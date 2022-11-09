from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
 
driver = webdriver.Chrome(ChromeDriverManager().install())

def twitter():
    filename = 'twitter.txt'
    outfile = 'twitter_out.csv'
    posts = []
    results = []
    with open(filename) as f:
        for line in f:
            posts.append(line)

    try:
        for post in posts:
            driver.get(post)
            driver.implicitly_wait(5)
            like = 0
            retweet = 0
            time = ""
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[3]/div[6]/div/div[3]/div/a/div/span/span/span")
            like = int(element.text.replace(',', ''))
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[3]/div[6]/div/div[1]/div/a/div/span/span/span")
            retweet = int(element.text.replace(',', ''))
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[3]/div[5]/div/div[1]/div/a[1]/time")
            time = element.text.split(" ")[2]
            results.append([time, post.replace('\n', ''), str(like), str(retweet)])
            print("Like: " + str(like) + " Retweet: " + str(retweet) + " Time: " + time)
            sleep(10)
    except:
        print("Error")
        print(post)
    finally:
        with open(outfile, 'w') as f:
            for result in results:
                f.write(result[0] + "," + result[1] + "," + result[2] + "," + result[3])
                f.write("\n")

def tiktok():
    filename = 'tiktok.txt'
    outfile = 'tiktok_out.csv'
    posts = []
    results = []
    with open(filename) as f:
        for line in f:
            posts.append(line)

    try:
        for post in posts:
            driver.get(post)
            driver.implicitly_wait(5)
            like = ""
            time = ""
            element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]/strong")
            like = str(element.text)
            if like.endswith("K"):
                like = like.replace("K", "")
                like = int(float(like) * 1000)
            else:
                like = int(like)
            element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div/a[2]/span[2]/span[2]")
            time = "2022/" + element.text.replace("-", "/")
            post = driver.current_url.split("?")[0]
            results.append([time, post.replace('\n', ''), str(like)])
            print("Like: " + str(like) + " Time: " + time + " Post: " + post)
            sleep(10)
    except:
        print("Error")
        print(post)
    finally:
        with open(outfile, 'w') as f:
            for result in results:
                f.write(result[0] + "," + result[1] + "," + result[2])
                f.write("\n")

# twitter()
tiktok()
