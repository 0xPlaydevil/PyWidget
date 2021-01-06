import pandas as pd
import PySimpleGUI as SG

class DealRecords:
    def __init__(self,filename='deal.csv'):
        self.df=self.load(filename)
    
    def load(self,filename):
        # gbk/cp936/ms936都一样,dtype=str导入防止数据失真
        df= pd.read_csv(filename,encoding='gbk',dtype=str)
        # 删除最后一列
        df.drop([df.columns[-1]],axis=1,inplace=True)
        # 修复列名
        colNames=[nm.rstrip() for nm in df.columns]
        colNameDic=dict(zip(df.columns,colNames))
        df.rename(columns=colNameDic,inplace=True)
        # print(df.columns)
        # 清理尾空格，修正特定列数据
        df= df.applymap(str.rstrip)
        df['证券代码']= df['证券代码'].str.strip('" =')
        # print(df['证券代码'])
        # 设定列类型
        df['成交数量']= df['成交数量'].astype(int)
        df['成交均价']= df['成交均价'].astype(float)
        df['成交金额']= df['成交金额'].astype(float)
        df.loc[:,'成交日期']= pd.to_datetime(df.loc[:,'成交日期'],format='%Y-%m-%d',errors='coerce')
        # print(df.dtypes)
        # 取子集
        df= df.loc[:,'成交日期':'股份余额']
        return df
    def corps(self):
        # 从列里取惟一性列表
        return self.df['证券名称'].unique().tolist()
    def corpcodes(self):
        return self.df['证券代码'].unique().tolist()
    def take(self,corp):
        # 获取分组后的一个子集
        return self.df.take(self.df.groupby(['证券名称']).groups[corp])

def main():
    dealRecs= DealRecords()
    corps=dealRecs.corps()
    layout= [[SG.Combo(corps,corps[0],(10,10),readonly=True,enable_events=True,k='-selcorp-'),
              SG.Spin(list(range(len(corps))),enable_events=True,k='-selcorpseq-')],
             [SG.Text('测试3')]]
    window= SG.Window('历史持仓',layout,size=(800,600))
    sel=window['-selcorp-']
    isel=window['-selcorpseq-']
    
    while True:
        event,values= window.Read(1000)
        if event==SG.WIN_CLOSED:
            break
        if event=='-selcorpseq-':
            sel.update(set_to_index=values['-selcorpseq-'])
        if event=='-selcorp-':
            isel.update(sel.Values.index(values['-selcorp-']))
    print(dealRecs.corps())