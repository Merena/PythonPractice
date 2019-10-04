**Django**：Python 界最全能的 web 开发框架，battery-include 各种功能完备，可维护性和开发速度一级棒。常有人说 Django 慢，其实主要慢在 Django ORM 与数据库的交互上，所以是否选用 Django，取决于项目对数据库交互的要求以及各种优化。而对于 Django 的同步特性导致吞吐量小的问题，其实可以通过 Celery 等解决，倒不是一个根本问题。Django 的项目代表：Instagram，Guardian。
		
**Tornado**：天生异步，性能强悍是 Tornado 的名片，然而 Tornado 相比 Django 是较为原始的框架，诸多内容需要自己去处理。当然，随着项目越来越大，框架能够提供的功能占比越来越小，更多的内容需要团队自己去实现，而大项目往往需要性能的保证，这时候 Tornado 就是比较好的选择。Tornado项目代表：知乎。
		
**Flask**：微框架的典范，号称 Python 代码写得最好的项目之一。Flask 的灵活性，也是双刃剑：能用好 Flask 的，可以做成 Pinterest，用不好就是灾难（显然对任何框架都是这样）。Flask 虽然是微框架，但是也可以做成规模化的 Flask。加上 Flask 可以自由选择自己的数据库交互组件（通常是 Flask-SQLAlchemy），而且加上 celery +redis 等异步特性以后，Flask 的性能相对 Tornado 也不逞多让，也许Flask 的灵活性可能是某些团队更需要的。