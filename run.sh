start=$SECONDS
python driver/driver.py $1 test_data/$2 True False False
#wait
echo $(( SECONDS - start ))
start=$SECONDS
python driver/driver.py $1 test_data/$2 False True False
#wait
echo $(( SECONDS - start ))
start=$SECONDS
python driver/driver.py $1 test_data/$2 True False True
#wait
echo $(( SECONDS - start ))
start=$SECONDS
python driver/driver.py $1 test_data/$2 False False False
wait
echo $(( SECONDS - start ))
start=$SECONDS
