def fetch_data_to_dataframe(symbol: str) -> pd.DataFrame:
    """
    外部APIからデータを取得し、Pandas DataFrameに変換する (ダミー実装)。

    Args:
        symbol: 取得する取引シンボル (例: 'BTC/USD')

    Returns:
        pd.DataFrame: 取得したデータ (インデックスはUTCのタイムスタンプ)
    """
    # 実際にはここで requests ライブラリなどを使ってAPIからデータを取得します
    
    # ダミーデータの生成
    data = {
        'timestamp': [
            dt.datetime(2025, 1, 1, 10, 0, 0),
            dt.datetime(2025, 1, 1, 11, 0, 0),
            dt.datetime(2025, 1, 1, 12, 0, 0)
        ],
        'open': [10000, 10050, 10100],
        'high': [10060, 10120, 10150],
        'low': [9950, 10040, 10090],
        'close': [10050, 10100, 10140],
        'volume': [100.5, 95.2, 110.0]
    }
    df = pd.DataFrame(data)
    
    # タイムゾーンの一貫性確保 (UTCで設定)
    # タイムスタンプ列をdatetime型にし、タイムゾーンをUTCに設定
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_localize('UTC')
    df = df.set_index('timestamp')
    
    print(f"[{symbol}] Data fetched and converted to DataFrame (UTC).")
    return df





def write_dataframe_to_sqlite(df: pd.DataFrame, table_name: str, db_path: str):
    """
    Pandas DataFrameの内容をSQLiteデータベースの指定テーブルに書き込む。

    Args:
        df: 書き込むPandas DataFrame。
        table_name: データベース内のテーブル名。
        db_path: SQLite DBファイルのパス (例: 'trading_data.db')
    """
    conn = None
    try:
        # DBに接続 (ファイルが存在しない場合は作成される)
        conn = sqlite3.connect(db_path)
        
        # DataFrameをSQLに書き込み
        # if_exists='append'で既存データに追加、index=TrueでDataFrameのインデックス(UTCタイムスタンプ)も保存
        df.to_sql(table_name, conn, if_exists='append', index=True, index_label='timestamp')
        
        print(f"DataFrame successfully written to table '{table_name}' in {db_path}.")
    
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        
    finally:
        if conn:
            conn.close()





def read_data_from_sqlite(table_name: str, db_path: str) -> Optional[pd.DataFrame]:
    """
    SQLiteデータベースからデータを読み込み、Pandas DataFrameとして返す。

    Args:
        table_name: データベース内のテーブル名。
        db_path: SQLite DBファイルのパス。

    Returns:
        Optional[pd.DataFrame]: 読み込んだデータ。失敗した場合はNone。
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        
        # SQLクエリで全データを取得
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn, index_col='timestamp')
        
        # タイムゾーンの一貫性確保 (UTCで復元)
        # DBにTEXTとして保存されたタイムスタンプをdatetime型に戻し、UTCとして認識させる
        df.index = pd.to_datetime(df.index).tz_localize('UTC')
        
        print(f"Data successfully read from table '{table_name}' and restored to DataFrame (UTC).")
        return df
    
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return None
        
    finally:
        if conn:
            conn.close()