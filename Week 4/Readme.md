## Assignment Steps

### 1. Prepare the mapper and reducer on cluster

After you create the mapper and reducer:

Type in the following to **open a text editor**, and then cut and paste the above lines for ```wordcount_mapper.py``` into the text editor, save, and exit. Repeat for ```wordcount_reducer.py```

```
gedit wordcount_mapper.py

gedit wordcount_reducer.py

```


**Enter the following to make it executable**

```
chmod +x wordcount_mapper.py

chmod +x wordcount_reducer.py
```

**Enter the following to see what directory you are in**

```
pwd

```

It should be /user/cloudera , or something like that.

### 2. Create some data:

```
echo "A long time ago in a galaxy far far away" > /home/cloudera/testfile1

echo "Another episode of Star Wars" > /home/cloudera/testfile2

```

This creates two text file on your local machine.

**NOTE:** ```/home/cloudera``` means LOCAL.

### 3. Create a directory on the HDFS file system

```
hdfs dfs -mkdir /user/cloudera/input
```

Important: If the directory is already there, you need to remove the existing directory or create new now. **HDFS doesn't handle overwriting.**

```
hdfs dfs -rm r /user/cloudera/input

# remove the directory.

```
### 5. Copy the files from local filesystem to the HDFS filesystem:

```

hdfs dfs -put /home/cloudera/testfile1 /user/cloudera/input

hdfs dfs -put /home/cloudera/testfile2 /user/cloudera/input

```

> **Again,** ```home/cloudera``` means local and ```user/cloudera``` means cluster.

### 6. You can see your files on HDFS
```
hdfs dfs -ls /user/cloudera/input

```

### 7. Run the Hadoop WordCount example with the input and output specified.

Note that your file paths may differ. The ‘\’ just means the command continues on next line.

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_new \
   -mapper /home/cloudera/wordcount_mapper.py \
   -reducer /home/cloudera/wordcount_reducer.py
```
This is called streaming, and note ``` -reducer /home/cloudera/wordcount_reducer.py ``` is the reducer count.

Hadoop prints out a whole lot of logging or error information. If it runs you will see something like the following on the screen scroll by:

....

> INFO mapreduce.Job: map 0% reduce 0%

> INFO mapreduce.Job: map 67% reduce 0%

> INFO mapreduce.Job: map 100% reduce 0%

> INFO mapreduce.Job: map 100% reduce 100%

> INFO mapreduce.Job: Job job_1442937183788_0003 completed successfully

### 8. Check the output file to see the results:

```
hdfs dfs -cat /user/cloudera/output_new/part-r-00000

```

-cat command is for checking content. -ls is listing.

### 9. View the output directory:

```
hdfs dfs -ls /user/cloudera/output_new
```

Look at the files there and check out the contents, e.g.:
```
hdfs dfs -cat /user/cloudera/output_new/part-r-00000
```

### 10. Streaming options:

Try:

```hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar --help
```

or see [hadoop.apache.org/docs/r1.2.1/](hadoop.apache.org/docs/r1.2.1/)

Let’s change the number of reduce tasks to see its effects. **Setting it to 0 will execute no reducer and only produce the map output.** (Note the output directory is changed in the snippet below because Hadoop doesn’t like to overwrite output)

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_new_0 \
   -mapper /home/cloudera/wordcount_mapper.py \
   -reducer /home/cloudera/wordcount_reducer.py \
   -numReduceTasks 0
 ```

 Get the output file from this run, and then upload it:

 ```
 hdfs dfs -getmerge /user/cloudera/output_new_0/* wordcount_num0_output.txt

 ```

###11. Change the number of reducers to 2 and answer the related quiz question at the end of the video lesson
