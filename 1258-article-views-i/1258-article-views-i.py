import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views["author_id"]==views["viewer_id"]][["author_id"]]
    # df=df.rename(columns={"author_id":"id"})
    # df["id"].unique()
    df.rename(columns={
        "author_id":"id"
    },inplace=True)
    df=df.sort_values(by="id")
    df=df["id"].unique()
    res=pd.DataFrame({'id':df})
    
    return res