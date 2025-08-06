# LangChain-Gemini

Bu projede Gemini kullanılmaktadır. Python sanal makina kurmanız gerekmektedir.
```bash
python -m venv .venv
```

# Bu projede iki farklı kullanım örneği bulunmaktadır:

 1) Hafızasız / Tek Seferlik:
    - Kullanıcıdan gelen sorgular tek seferlik işlenir.
    - create_react_agent(model, tools) ile agent çalıştırılır.
    - Önceki mesajlar veya thread geçmişi kaydedilmez.
    - TavilySearchResults aracı ile ilgili aramalar yapılabilir, ancak bazı durumlarda ilk sorgudan sonra tekrar kullanılmayabilir.
    - Model: gemini-2.0-flash, Temperature: 0.7

2) Hafızalı / Chat-Like:
    - InMemoryChatMessageHistory kullanılarak sohbet geçmişi tutulur.
    - Kullanıcı her mesaj gönderdiğinde önceki mesajlar da modele iletilir ve bağlama dayalı cevaplar alınır.
    - SystemMessage ile asistan rolü başlangıçta belirlenir.
    - Kullanıcı çıkana kadar devam eden chat-like kullanım sağlar.
    - Model: gemini-2.0-flash, Temperature: 0.7

## Ortam Değişkenleri (`.env`)
```env
GEMINI_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Your project name
TAVILY_API_KEY=your_key
```

.env dosyasını kaydedin ve ana Python dosyasını çalıştırmadan önce yükleyin.

Hafızalı projede çıkmak için 'exit' veya 'quit' yazabilirsiniz.

