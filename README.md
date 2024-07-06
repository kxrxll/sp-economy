### Паутинообразная модель экономической динамики

В задачах оптимизации экономической динамики анализируются изменение экономических параметров и их взаимосвязей во времени. В моделях экономической динамики время может рассматриваться как дискретное изменяющееся скачком, например, за год. Для описания таких процессов используются разностные уравнения. При непрерывном изменении во времени для описания параметров модели используются дифференциальные уравнения.

Паутинообразная модель позволяет исследовать устойчивость цен и объемов производства на рынке, описываемом кривыми спроса и предложения некоторого товара. Функция спроса S(p) характеризует зависимость объема спроса на товар от цены р товара в данный период i. Функция предложения D(p) характеризует объем предложения товара в зависимости от цены товара. Равновесная цена р, рынка определяется равенством спроса и предложения S(p) = D(p).

Производитель определяет объём предлагаемого товара исходя из спроса и цен на товар установившихся в предыдущем периоде – i-1. Для решения этого уравнения зададим объём в начальный период Q0 и используя обратную функцию предложения определим цену на товар. Объём производства в следующий период времени определим через функцию спроса и так далее. Если функции спроса и предложения меняются, то колебания цен будут определятся только отклонением цены от равновесной.

#### Вывод

Корректируя постоянные a, b по статистике работы рынка товаров (такой анализ хорошо разработан в scipy.stats) паутинообразную модель можно использовать для корректировки объёмов производства.
