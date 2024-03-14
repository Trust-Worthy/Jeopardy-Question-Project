import pandas as pd
import numpy as np
import random
import jeoparday_df_info as JDF_INFO

# length of the data frame

# number of episodes in the dataset  


def create_df():
    

    # initialize dataframe from csv
    question_df = pd.read_csv("JEOPARDY_CSV.csv")

    # storing total number of questions in JDF_INFO_ENUM
    JDF_INFO.JDF_INFO_ENUM.TOTAL_NUM_QUESTIONS = len(question_df)

    # storing first 10 entries of dataframe in JDF_INFO_ENUM
    JDF_INFO.JDF_INFO_ENUM.FIRST_10_ENTRIES = str(question_df.head(10))
    # storing last 10 entires of dataframe in JDF_INFO_ENUM
    JDF_INFO.JDF_INFO_ENUM.LAST_10_ENTRIES = str(question_df.tail(10))

    # storing totoal number of episodes in JDF_INFO_ENUM
    first_epi_num = question_df['Show Number'][0]
    last_epi_num = question_df['Show Number'][len(question_df)]
    JDF_INFO.JDF_INFO_ENUM.TOTAL_NUM_EPISODES = last_epi_num - first_epi_num
    

    return question_df


def jeopardy_df_main():
    question_df = create_df()
    #show_df_info(question_df)
    get_num_episodes(question_df)


if __name__ == "__main__":
    jeopardy_df_main()