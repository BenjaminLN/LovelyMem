import sqlite3
import yaml
import os
import shutil

with open('config/base_config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

symbols_path = config['tools']['volatility3_symbols']['path']
symbols_path = os.path.abspath(symbols_path)
symbols_path = symbols_path.replace("\\", "/")


def update_identifier_cache():
    shutil.copy("db/identifier.cache", "db/identifier_new.cache")
    try:
        conn = sqlite3.connect('db/identifier_new.cache')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cache
            SET location = REPLACE(location, 'E:/Tools/volatility3/symbols', ?)
        """, (symbols_path,))
        conn.commit()
        print("volatility3数据库更新成功")

    except sqlite3.Error as e:
        print(f"更新数据库时出错: {e}")
    finally:
        if conn:
            conn.close()
    user_home = os.path.expanduser('~')
    target_path = os.path.join(user_home, 'AppData', 'Roaming', 'volatility3')
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if os.path.exists(os.path.join(target_path, "identifier.cache")):
        os.remove(os.path.join(target_path, "identifier.cache"))
    shutil.copy("db/identifier_new.cache", target_path)
    os.rename(os.path.join(target_path, "identifier_new.cache"), os.path.join(target_path, "identifier.cache"))

update_identifier_cache()
