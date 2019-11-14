# chatbot-deeplearning

This project is a collaborated effort to learn the tools to perform Deep Learning in Brandeis Codestellation hackathon 2019 by creating a chatbot.

Our learning data is from Reddit 2015-01 comments: https://mega.nz/#!ysBWXRqK!yPXLr25PgJi184pbJU3GtnqUY4wG7YvuPpxJjEmnb9A
If you are interested in using a large data to train the bot, here's the link to ~1.7 billion comments (250 GB compressed): https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/?st=j9udbxta&sh=69e4fee7
We are using nmt-chatbot library (https://github.com/daniel-kukiela/nmt-chatbot) which allows us to train the bot with our data using NMT - Neural Machine Translation (seq2seq).
The project requires the use of TensorFlow.

Since the data and training files themselves are too big for Github, we will instruct you how to replicate our projects (if you're interested):
1. Download the Reddit data and put it in the project folder (src)
2. Run python main.py (it will take a while since there are 53,851,542 total comments, taking up ~32 GB uncompressed)
I created the file to facilitate the creation of training (and testing) data files.
It will first read the data, using it to create a SQLite database.
After that, it will pull data from the database to create training and testing files (.from and .to). 
Feel free to modify the queries if you would like to train the bot to be less "general" (query from specific subreddit(s), for example)
3. Replace the training and testing files in nmt_chatbot/new_data
- train.from and train.to (taken from our train.from and train.to, no need to rename the files)
- tst2012.from, tst2013.from and tst2012.to, tst2013.to (taken from test.from and test.to, rename our files to replace the current ones in the directory)
4. Edit nmt_chatbot/setup/settings.py (optional)
5. Run python nmt_chatbot/setup/prepare_data.py
6. Run python nmt_chatbot/train.py 
This will take a long time (depending on your computer and the settings)
You can test by running python inference.py, which will create an interactive environment with your current chatbot model in our console
7. I created a function 'interact()' which will use the inference file (after the training) to access the final chatbot


