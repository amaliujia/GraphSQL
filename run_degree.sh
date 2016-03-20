start=$SECONDS
python driver/driver.py $1 test_data/$2 True False False
#wait
echo $(( SECONDS - start ))
