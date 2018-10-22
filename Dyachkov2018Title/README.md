# Cross-Language Document Extractive Summarization with Neural Sequence Model 

Захаров П.С, Пискун М.Г., Сельницкий И.С., Кваша П.А., Дьячков Е.А, Петров Е.Д.

Московский физико-технический институт

## Абстракт

В данной работе рассматривается алгоритм выделения ключевых аспектов текста на языке, отличным от того, что используется в самой статье. Построенная модель производит сокращение текста, выделяя в нем главное, а затем применяет к полученному изложению перевод. При этом исследуется зависимость качества полученного результата от качества перевода. Помимо этого, в работе рассматривается переносимость построенной модели на данные, представленные на других языках.


## Введение

На сегодняшний день в мире существует 2 проблемы: 

* Огромное количество информации, представленной в несжатом виде
* Эта информация представлена на разных языках

&nbsp;&nbsp;&nbsp;&nbsp;Первая проблема привелы к развитию машинного сокращения текстов, вторая - к машинному переводу. Необходимость делать сокращения текстов на других языках привела к исследованиям по совмещению этих двух алгоритмов. Наиболее простым решением на сегодняшний день является последовательное их применение: сокращения текста на языке оригинале и перевод на требуемый язык либо в другом порядке. Данные модели соответсвенно получили названия **LateTrans** и **EarlyTrans**. Обе модели показывали неважные результаты в связи с несовершенством скомбинированной модели. Неидеальный выход одной модели подвергался еще большему искажению на второй. Однако Wan [[5]](https://github.com/Intelligent-Systems-Phystech/2018-Project-29/tree/master/Dyachkov2018Title#5-xiaojun-wan-using-bilingual-information-for-cross-language-document-summarization-in-proceedings-of-the-49th-annual-meeting-of-the-association-for-computational-linguistics-human-language-technologies---volume-1-hlt-11-pages-15461555-stroudsburg-pa-usa-2011-association-for-computational-linguistics) предложил одновременно ранжировать предложения на исходном языке и на языке, на который надо перевести.

&nbsp;&nbsp;&nbsp;&nbsp;В данной работе мы нацелены на создании модели, позволяющей делать краткую выжимку по английскому тексту на русском языке. Входными параметры - наборы текстов на английсклм языке, выходные - краткое его изложение на русском. Но так как качество машинного перевода далеко неидеально, это вносит опеределенные трудности в изложении текста на разных языках, так как ошибки и шумы перевода отрицательно влияют на оценку качество сжатого текста.

&nbsp;&nbsp;&nbsp;&nbsp;В нашем иссследовании мы хотим применить предложенную Nallapati [[2]](https://github.com/Intelligent-Systems-Phystech/2018-Project-29/tree/master/Dyachkov2018Title#2-ramesh-nallapati-feifei-zhai-and-bowen-zhou-summarunner-a-recurrent-neural-network-based-sequence-model-for-extractive-summarization-of-documents-corr-abs161104230-2016) и существенно улучшенную позже [[4]](https://github.com/Intelligent-Systems-Phystech/2018-Project-29/tree/master/Dyachkov2018Title#4-pengjie-ren-zhumin-chen-zhaochun-ren-furu-wei-jun-ma-and-maarten-de-rijke-leveraging-contextual-sentence-relations-for-extractive-summarization-using-a-neural-attention-model-in-proceedings-of-the-40th-international-acm-sigir-conference-on-research-and-development-in-information-retrieval-sigir-17-pages-95104-new-york-ny-usa-2017-acm) модель сокращения текстов SummaRuNNer. Предлагается развить идею Wan [[6]](https://github.com/Intelligent-Systems-Phystech/2018-Project-29/tree/master/Dyachkov2018Title#6-xiaojun-wan-huiying-li-and-jianguo-xiao-cross-language-document-summarization-based-on-machine-translation-quality-prediction-in-proceedings-of-the-48th-annual-meeting-of-the-association-for-computational-linguistics-acl-10-pages-917926-stroudsburg-pa-usa-2010-association-for-computational-linguistics) в приминении к сокращению английского текста с результатом на русском языке. Обучение построенной модели будет происходить на данных CNN/DailyMail corpus.

## Список литературы

###### [1] Guillaume Klein, Yoon Kim, Yuntian Deng, Jean Senellart, and Alexander M. Rush. Opennmt: Open-source toolkit for neural machine translation. CoRR, abs/1701.02810, 2017.

###### [2] Ramesh Nallapati, Feifei Zhai, and Bowen Zhou. Summarunner: A recurrent neural network based sequence model for extractive summarization of documents. CoRR, abs/1611.04230, 2016.

###### [3] Elvys Linhares Pontes, St´ephane Huet, Juan-Manuel Torres-Moreno, and Andr´ea CarneiroLinhares. Cross-language text summarization using sentence and multi-sentence compression.In Natural Language Processing and Information Systems, pages 467–479. Springer International Publishing, 2018.

###### [4] Pengjie Ren, Zhumin Chen, Zhaochun Ren, Furu Wei, Jun Ma, and Maarten de Rijke. Leveraging contextual sentence relations for extractive summarization using a neural attention model. In Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’17, pages 95–104, New York, NY, USA, 2017. ACM.

###### [5] Xiaojun Wan. Using bilingual information for cross-language document summarization. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies - Volume 1, HLT ’11, pages 1546–1555, Stroudsburg, PA, USA, 2011. Association for Computational Linguistics.

###### [6] Xiaojun Wan, Huiying Li, and Jianguo Xiao. Cross-language document summarization based on machine translation quality prediction. In Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics, ACL ’10, pages 917–926, Stroudsburg, PA, USA, 2010. Association for Computational Linguistics.
