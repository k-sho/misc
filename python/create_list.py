from pathlib import Path
import os
import pandas as pd
import argparse

def create_list(path, dest="dest.csv"):
    df = pd.DataFrame(columns=['path', 'size'])
    artifacts = Path(path).glob('**/*')
    for ap in artifacts:
        if ap.is_file():
            s = pd.Series([ap.relative_to(path), os.path.getsize(ap)], index=df.columns)
            df = df.append(s, ignore_index=True)
    df.to_csv(dest, index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('installpath', type=str)
    parser.add_argument('--dest', type=str)
    args = parser.parse_args()

    installpath = args.installpath
    destpath = args.dest
    
    if destpath == None:
        create_list(installpath)
    else:
        create_list(installpath, destpath)

main()
