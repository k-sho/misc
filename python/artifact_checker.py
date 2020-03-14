import pandas as pd
import argparse

def artifact_check(source1, source2, dscale=100000):
    df1 = pd.read_csv(source1)
    df2 = pd.read_csv(source2)
    
    df_merge = df1.merge(df2, on='path', indicator=True, how='outer')    

    df_l = df_merge.query("_merge == 'left_only'")
    df_l[["path", "size_x"]].to_csv("left_only.csv", index=False)
    
    df_r = df_merge.query("_merge == 'right_only'")
    df_r[["path", "size_y"]].to_csv("right_only.csv", index=False)

    df_both = df_merge.query("_merge == 'both'")[["path", "size_x", "size_y"]]
    df_both[["path", "size_x", "size_y"]].to_csv("both.csv", index=False)

    df_diff = df_both.query("size_x != size_y")
    print("The following files are %d bytes smaller than right." % dscale)
    print(df_diff.query("size_y - size_x <= -1 * %d" % dscale))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('left', type=str)
    parser.add_argument('right', type=str)
    parser.add_argument('--dscale', type=int)
    args = parser.parse_args()
    
    if args.dscale == None:
        artifact_check(args.left, args.right)
    else:
        artifact_check(args.left, args.right, args.dscale)

main()
