# Sentiment Analysis on Covid19 Vaccination


# Datasets

## Raw Dataset

[raw_dataset.csv](raw_dataset.csv) contains crawled data from Twitter based on tweets containing “#vaccine”. 

### Bronze Dataset

[bronze_dataset.csv](bronze_dataset.csv) contains dataset after text preprocessing and language detection.

### Silver Dataset

[silver_dataset.csv](silver_dataset.csv) contains tweets tweets from 1st January 2021 to 31st March 2021. 

[silver_dataset_polarity_output.csv](silver_dataset_polarity_output.csv) contains tweets from Silver Dataset with Polarity API output for each sample (Excludes some tweets showing error in the API).

[silver_output.csv](silver_output.csv) contains outputs from `NLTK VADER`, `Text Blob` and `Flair` corresponding to each tweet.

### Gold Dataset

[gold_dataset.csv](gold_dataset.csv) contains Annotated data of 500 tweets.

[gold_output.csv](gold_output.csv) contains outputs from `NLTK VADER`, `Text Blob` and `Flair` corresponding to each tweet in Gold Dataset.
