
for k in 0.2 2.0
do
for b in 0.0 1.0
do
wget  -O a.txt "http://clueweb.adaptcentre.ie/IRModelGenerator/TrecBatchQueryExecuterServlet?treccode="$3"&simf=BM25&k="$k"&b="$b
wget -O res_6.$k"."$b".txt" http://clueweb.adaptcentre.ie/IRModelGenerator/res.6.BM25.$k"."$b

../trec_eval $1 res_6.$k"."$b".txt" > a1.txt
echo $k","$b","`grep -m 1 "map" a1.txt | awk '{print $3}'` >> test.csv 
rm a1.txt
done
done
echo >> test.csv
cat test.csv | awk -F ',' '{if (NF>0) print $2}'|sort -n|uniq > tmp
cat tmp | awk 'BEGIN{printf(",");} {printf("%s,",$1);}' > $2".csv"

cat test.csv | awk -F ',' 'BEGIN{p=""; } {if($1!=p || NF==0) {print p"," a; a=$3} else {a = a "," $3} p=$1;}' >>$2".csv" 
rm tmp
rm test.csv
