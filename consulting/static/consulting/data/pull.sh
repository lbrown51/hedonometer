for FOLDER in breyers # $(\ls -1 keywords) # flavor
do
    # scp areagan@bluemoon-user1.uvm.edu:fun/twitter/unilever/keywords/${FOLDER}/tweets/*happs*-sum.csv keywords/${FOLDER}
    # scp areagan@bluemoon-user1.uvm.edu:fun/twitter/unilever/keywords/${FOLDER}/tweets/01.01.14-word-vector*-sum.csv keywords/${FOLDER}
    rsync -avzr areagan@bluemoon-user1.uvm.edu:fun/twitter/unilever/keywords/${FOLDER}/tweets/*word-vector*-sum.csv keywords/${FOLDER}
    # scp areagan@bluemoon-user1.uvm.edu:fun/twitter/unilever/keywords/${FOLDER}/tweets/*frequency*-sum.csv keywords/${FOLDER}
done