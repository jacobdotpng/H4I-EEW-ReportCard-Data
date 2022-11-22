from generate_scores import clone_repo, gen_score_safe
import pandas as pd
import subprocess


def main():
    clone_repo()
    #run_all_districts()
    demo()


def run_all_districts():
    """
    Loops through all of the congressional districts in all states and calls gen_report(state, cd) on them
    """
    file_name = "../state_cd.csv"
    df = pd.read_csv(file_name)
    # Find all unique values of first column of CSV file (all unique states in a given CSV file)
    states = df.iloc[:,0].unique()
    # Loop through each state in the CSV & find all unique districts in that state
    for state in states:
        dists = df[df.iloc[:,0] == state].iloc[:,1].unique()
        # Gen_report for each unique state, district pair
        for cd in dists:
            # Utilize size of log file to pause and start program
            # Get size of "logs/score_geenerations_log.txt" file
            log_size = subprocess.check_output("wc -c logs/score_generation_logs.txt", shell=True)

            # Use run_AllPrograms to generate report card & consequently create logs for score generation
            state_cd = str(state) + "," + str(cd)
            subprocess.call(["sh", "../run_AllPrograms.sh", state_cd])

            new_log_size = subprocess.check_output("wc -c logs/score_generation_logs.txt", shell=True)
            # If log file size has not changed, pause program
            while log_size == new_log_size:
                new_log_size = subprocess.check_output("wc -c logs/score_generation_logs.txt", shell=True)

def demo():
    """
    Loops through all of the congressional districts in all states and calls gen_report(state, cd) on them
    """
    file_name = "../state_cd.csv"
    df = pd.read_csv(file_name)
    # Find all unique values of first column of CSV file (all unique states in a given CSV file)
    states = df.iloc[:,0].unique()
    # Loop through each state in the CSV & find all unique districts in that state
    for state in states:
        dists = df[df.iloc[:,0] == state].iloc[:,1].unique()
        # Gen_report for each unique state, district pair
        for cd in dists:
            # Utilize size of log file to pause and start program
            # Get size of "logs/score_geenerations_log.txt" file
            log_size = subprocess.check_output("wc -c logs/score_generation_logs.txt", shell=True)

            gen_score_safe(state, cd)

            new_log_size = subprocess.check_output("wc -c logs/score_generation_logs.txt", shell=True)
            # If log file size has not changed, pause program
            while log_size == new_log_size:
                new_log_size = subprocess.check_output("wc -c logs/score_generation_logs.txt", shell=True)



if __name__ == "__main__":
    main()

