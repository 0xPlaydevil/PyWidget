import pandas as pd
import PySimpleGUI as SG

class DealRecords:
    def __init__(self,filename='deal.csv'):
        self.df=self.load(filename)
        self.corpinfos=self.corpinfos()
    
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
        # df['成交数量']= df['成交数量'].astype(int)
        # df['成交金额']= df['成交金额'].astype(float)
        # df.loc[:,'成交数量':'股份余额'].apply(pd.to_numeric,inplace=True)
        df.loc[:,'成交数量':'股份余额']=df.loc[:,'成交数量':'股份余额'].apply(pd.to_numeric)
        df.loc[:,'成交日期']= pd.to_datetime(df.loc[:,'成交日期'],format='%Y-%m-%d',errors='coerce')
        df['成交均价']= df['成交均价'].astype(float)
        # print(df.dtypes)
        # 取子集
        df= df.loc[:,'成交日期':'股份余额']
        return df
    
    def corpinfos(self):
        df= pd.DataFrame({'name':self.df['证券名称'].unique(),'code':self.df['证券代码'].unique()})
        curprofits=[]
        for i in range(df.shape[0]):
            df_corp=self.take(df['name'][i],True)
            curprofits.append(df_corp['profit'].iat[-1])
        df['curprofit']=pd.Series(curprofits)
        return df
        
    def corps(self,rank=0):
        if rank== 0:
            return self.corpinfos['name'].tolist()
        if rank== 1:
            return self.corpinfos.sort_values('curprofit')['name'].tolist()
        if rank== 2:
            return self.corpinfos.sort_values('curprofit',ascending=False)['name'].tolist()

    def corpcodes(self):
        return self.df['证券代码'].tolist()
    def take(self,corp,analysis=False):
        # 获取分组后的一个子集
        df_corp= self.df.take(self.df.groupby(['证券名称']).groups[corp])
        if not analysis:
            return df_corp
        else:
            # 复制一份。直接df=df_corp报警告：A value is trying to be set on a copy of a slice from a DataFrame
            df=pd.DataFrame(df_corp)
            df['direc']=df['委托方向']
            # 提取委托方向
            df['委托方向']=df['委托方向'].str.get(3)
            df.loc[df['委托方向']=='出','direc']=-1
            df.loc[df['委托方向']=='入','direc']=1
            df['direc']=df['direc'].astype(float)
            # 为成交金额添加方向
            df['trading_volumn']=df['成交金额'].mul(df['direc'])
            # 翻转数据
            df= df.iloc[::-1]
            df.index=range(len(df))
            # 生成当前成本列
            df['curcost']= df['trading_volumn'].cumsum()
            # 生成收益列
                # 发现东方财富客户端导出表的股份余额列有错，同一天连续两次买入，股份余额会反
            df['股份余额修正']= (df['成交数量']*df['direc']).cumsum()
            df['profit']= df['股份余额修正']*df['成交均价']-df['curcost']
            return df
            

def main():
    dealRecs= DealRecords()
    rankmap= {'不排序':0, '升序':1, '降序':2}
    corps=dealRecs.corps()
    layout= [[SG.Combo(corps,corps[0],(10,10),readonly=True,enable_events=True,k='-selcorp-'),
              SG.Spin(list(range(len(corps))),size=(3,1),enable_events=True,k='-selcorpseq-'),
              SG.Combo(list(rankmap.keys()),list(rankmap.keys())[0],(6,3),readonly=True,enable_events=True,k='-cmbRank-')],
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
        if event== '-cmbRank-':
            sel.update(values=dealRecs.corps(rankmap[values['-cmbRank-']]))
        if event in ['-selcorp-','-cmbRank-']:
            isel.update(sel.Values.index(values['-selcorp-']))

pd.set_option('display.float_format',lambda x:'%.2f' % x)

main()
