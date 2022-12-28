from gensim.summarization.summarizer import summarize # gensim 3.7.3 이후 버전에는 요약이 없음
import base64, textwrap, re, collections, webbrowser, os


if __name__ == "__main__":

    # 이미지
    f = open("image/image.jpg","rb")
    image = f.readline()
    print(image)
    f.close()

    # 기사 본문
    f = open("news/article", 'b')
    news = f.readline()
    f.close()

    # 기사 이미지 디코딩
    path = "../../../1year/mini-program/뉴스-기사-요약/image/image.jpg"
    file_image = image[0]

    with open(path, 'wb') as f:
        decoded_data = base64.decodebytes(file_image)
        f.write(decoded_data)

    # 기사 본문 디코딩
    file_news = news[0]
    decoded_data = base64.decodebytes(file_news)
    news = decoded_data.decode('utf-8')

    # 요약 텍스트 저장
    # (https://github.com/Kyubyong/wordvectors)
    # 사전 학습모델 가지고 옴
    news_summarized = summarize(news, ratio=0.1)

    # 줄바꿈 정렬
    article_align = textwrap.fill(news, width=50)

    # 단어 추출
    words = re.findall(r'\w+', article_align)

    # 빈도수 산출
    counter = collections.Counter(words)

    # 키워드 추출
    keywords = counter.most_common(5)[1:]
    keys = ['# ' + elem[0] for elem in keywords]
    keys = ' '.join(keys)

    # html 파일 저장
    htmlfile = open("news/summary.html", "w")
    htmlfile.write("<html>\n")
    htmlfile.write("<h1>" + '뉴스 요약' + "</h2>\n")
    htmlfile.write("<img src='image.jpg'/>\n")
    htmlfile.write("<h2>" + news_summarized + "</h2>\n")
    htmlfile.write("<h2 style='background-color:powderblue;''>" + keys + "</h2>\n")
    htmlfile.write("</html>\n")
    htmlfile.close()

    webbrowser.open('file://' + os.getcwd() + "/news/summary.html")
