import requests
import pandas as pd
from pandas.io.json import json_normalize

headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '__auc=c5035a4c16fd460dc07ce0577a8; _ga=GA1.2.1675266079.1579816115; _gid=GA1.2.130433663.1579816115; _hjid=d8db62c6-5395-4792-b978-f8acad779132; G_ENABLED_IDPS=google; __stripe_mid=9c010cef-ed83-4d45-b43c-c503185f7286; deal_merchant_context=bjlQcWtzZjRUOVUwSkd2a2Q5UVZaQT09LS1iS21HdHlvc3dnTFozMUk0Vm4zYUd3PT0%3D--af41bf85604d65df31e1a087856436a7458f8fa0; recently_viewed=dFJZL28wSlpBbWZxM0lhV29Ndmo1eG1uT2locmYzSnFRNnZ5RTV3VHoyY1NkZkFOY2dBSzhpcDl0N3paaE9Cakk4ajR3aXVsbnU2S0pHaXR3MGkvNzhJb21rckpxR3pEVmg3NktJSXBLaXpXUkRqdHlPOGJBNm9ld1dEcHVNMEtDbGtlSHdrMUd5ZGh5dnVZL1AvbFh6THVUbHp5Smx5MXlGZU9iREtzREpKRVZ3ckhEKytKRDM2RTlFNlNvTEh3cE9xM200OTc4K2ZLTk1EU1VCK09BS3NabVo2TG5qWmg5SGRFWndTZjNLWXZpVXRtalhvemRKM2dyb1JNMDhKQXJxbEdIb0lpU25RUHp1Si9wSElrdFE9PS0tc0UzQ1gyeDViZTBTRTRZVjJJdm5ZUT09--c5812ca2bd7329c13efd31f5d2857d2d350cca4f; client_cache_key=bjRJRU50Smp4QllWZWZSZEN5U0dSaFZtZUdYUFhLeU1waVNxWlZzeVZMcz0tLVh5Tk43Q2R0OGxUL3hhdU9sM25rTUE9PQ%3D%3D--dcb0317e19a27dd55c032f3469330257f231aa18; __asc=1d3a125116fda03bf8ec3ab44e7; _derived_epik=dj0yJnU9cTREcURvekxVdWgxV0hwRkVNdS01OHdydVlVV0NqdEkmbj04MFFOQ09QUnduSFMtX0t4eHZjXzJ3Jm09NyZ0PUFBQUFBRjRyaGhR; _hp2_id.3503103446=%7B%22userId%22%3A%221682039594803097%22%2C%22pageviewId%22%3A%224355036978439434%22%2C%22sessionId%22%3A%227569355054565139%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.3503103446=%7B%22r%22%3A%22https%3A%2F%2Fwww.vivino.com%2Fexplore%3Fe%3DeJwdyjkKgDAURdHdvFKMQ_k6dyBWIvKNMQSMShIcdq_Y3NNcH1hmNbzbqHJ4uVnl0A-7FvpLg4MKduEpwZkkK_aJQZLbbBzlNEGswc7ZRI0r9cM3_xSI1PICdrAezQ%3D%3D%22%2C%22ts%22%3A1579910677732%2C%22d%22%3A%22www.vivino.com%22%2C%22h%22%3A%22%2Fexplore%22%2C%22q%22%3A%22%3Fe%3DeJwdyjkKgDAURdHdvFKMQ_k6dyBWIvKNMQSMShIcdq_Y3NNcH1hmNbzbqHJ4uVnl0A-7FvpLg4MKduEpwZkkK_aJQZLbbBzlNEGswc7ZRI0r9cM3_xSI1PICdrAezQ%3D%3D%22%7D; _ruby-web_session=WEVrV0tKSTF0WENUelFEbkJhNWcvQ1FLREszUCthSHYxQlZ3U1FLcE1UOTNNMHRyUmhDMmNobzlnUnZTZ2FJOXlwTWcrRUx1SzhuV29xYjJVUHBSSERBclplVkwybWxDRjFqT1FyOXFZQy9lRlg5dzB6RnpMZU5nWVJZVk1Xd3JIZm9MdHJVY3hPN2hobElVaXA4UzJLMC9IdFZ2ejBiV3pObTZ5Z1c2dTNaQllhWHdwQ1MrNW41cnlPWk5PcFIvVmxXd0F2VEVaT1dNZ0xqbHdtRTlNdkRsWVcvTEY1eGJSL2J6M254YTJIRm1HaHdob3NEa3hISHBpa3NHR0pVU0FLUzUwSWZMa2xGVVJRMklEVC9DdjRUd0drOWVJK3JkUE5aWkJ5bjF5N0kwcXo0amRUbUc0ZDdnT1cyRTJIbVl2MkZqL1Z0MTh2c09jeG9BWGVXa1Q4QWpvWDRwLzF4cXBjVXp4cmhDR2lFSXNyT2l4ZGtKK3liUUZydGd6ODhILS1DNGtFR1p5dm9QYlF3NkxtaGZnVUFBPT0%3D--d12cf4a96fb3bdab033a69f023265c2d009df0d4if-none-match: W/"0d29d1e750e26bd001dfced1286a95f6"',
    'referer': 'https://www.vivino.com/explore?e=eJwdyjkKgDAURdHdvFKMQ_k6dyBWIvKNMQSMShIcdq_Y3NNcH1hmNbzbqHJ4uVnl0A-7FvpLg4MKduEpwZkkK_aJQZLbbBzlNEGswc7ZRI0r9cM3_xSI1PICdrAezQ==',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

p = {
    'country_code': 'US',
    'currency_code': 'USD',
    'grape_filter': 'varietal',
    'min_rating': '1',
    'order_by': 'ratings_average',
    'order': 'desc',
    'page': '1',
    'price_range_max': '500',
    'price_range_min': '0',
    'wine_type_ids[]': '1',
    'wine_type_ids[]': '2',
}



def main():

    a = int(p['page'])
    df = pd.DataFrame()

    while a < 2000:
        p['page'] = str(a)
        a += 1

        try:
            r = requests.get(
                'https://www.vivino.com/api/explore/explore?country_code=MX&currency_code=MXN&grape_filter=varietal&min_rating=3.5&order_by=ratings_average&order=desc&page=1&price_range_max=400&price_range_min=100&wine_type_ids[]=1&wine_type_ids[]=2',
                headers=headers, params=p)
            complete_json = r.json()
            print('success')

            # normalize and clean up the data a little bit before sending to the dataframe
            df_data = pd.DataFrame.from_dict(json_normalize(complete_json['explore_vintage']['matches']), orient='columns')
            df = df.append(df_data)

        except:
            False

    df.to_excel('output.xlsx', encoding='utf8')
    df.to_csv("output.csv")
    print(df['vintage.name'].to_csv(index=False))


if __name__ == '__main__':
    main()


