最近在学习flask，其中教程推荐的测试工具是pytest，这里对其中一个重要的特性fixture作一些了解，资料来源是[官方文档](https://docs.pytest.org/en/latest/fixture.html)。

如果你是在GitHub上看到的文章，因为是在CSDN上写的，可以在这里跳转到[CSDN的文章下](http://blog.csdn.net/huitailang1991/article/details/74053781)。

# 1. fixture的目的
为可靠的和可重复执行的测试提供固定的基线。（可以理解为测试的固定配置，使不同范围的测试都能够获得统一的配置。）

fixture提供了区别于传统单元测试（setup/teardown）风格的令人惊喜的功能：

1. 有独立的命名，可以按照测试的用途来激活，比如用于functions/modules/classes甚至整个project。（我遇到的scope主要是session和function）。
2. 按模块单元的方式实现，每个fixture name可以出发一个fixture function，每个fixture function本身也能调用其他的fixture function。（相互调用，不只是用于test_func()）。
3. fixture的范围覆盖简单的单元测试到复杂的功能测试，可用于参数传入或者class、module及test session范围内的复用。

额外的，pytest也支持[传统的单元测试风格
](https://docs.pytest.org/en/latest/xunit_setup.html#xunitsetup)。可以混合使用风格，也可以从已存在的unit.TestCase style或nose based projects出发修改。

# 2. 作为参数传入
fixture装饰的函数可以作为参数传入其他的函数。简单的例子：

```python
# content of ./test_smtpsimple.py
import pytest

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0 # for demo purposes
```

# 3. 在module/class/session间共享一个 fixture

加入scope='module'的参数，可以让fixture function在每次模块测试的时候只请求一次。这样不同的test function在同一个test module中接收到的 `smtp`fixture参数都是一样的。

为了方便配置和访问，将这样的fixture放到`conftest.py`文件中单独存放。

```python
# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp():
    return smtplib.SMTP("smtp.gmail.com")
```
在`conftest.py`所处的目录下：
```python
# content of test_module.py

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes

def test_noop(smtp):
    response, msg = smtp.noop()
    assert response == 250
    assert 0  # for demo purposes
```

如果想要session范围的`smtp`实例，返回的fixture value将会在所有需要的测试间共享：
```python
@pytest.fixture(scope="session")
def smtp(...):
    # the returned fixture value will be shared for
    # all tests needing it
```

# 4. fixture的终止/执行teardown

当fixture超出scope指定的范围时，pytest支持执行指定的终结代码。用yield代替return，所有*yield*语句之后的代码执行类似teardown的情况：
```python
# content of conftest.py

import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp():
    smtp = smtplib.SMTP("smtp.gmail.com")
    yield smtp  # provide the fixture value
    print("teardown smtp")
    smtp.close()
```
上面`print`和`smtp.close()`语句会在module范围内的最后一个测试完成后执行，不管测试中有没有exception的状态。
如果我们在装饰器中指定`scope="function"`，那么`stmp`将会在每次单个测试中建立和清除。

这里`yield`也可以配合`with`语句使用：
```python
# content of test_yield2.py

import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        yield smtp  # provide the fixture value
```
`smtp`连接会在测试执行完后，会在`with`语句结束后自动关闭。
**Note： 如果在yield语句之前的setup code有exception发生，则yield语句之后的teardown code不会被执行。**

其他可供选择的`teardown code`的办法，在[request-context](https://docs.pytest.org/en/latest/fixture.html#request-context)对象中注册`addfinalizer`方法实现终结函数。
```python
# content of conftest.py
import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp(request):
    smtp = smtplib.SMTP("smtp.gmail.com")
    def fin():
        print ("teardown smtp")
        smtp.close()
    request.addfinalizer(fin)
    return smtp  # provide the fixture value
```
`yield`和`addfinalizer`方法都是在测试完成后呼叫相应的代码。但是`addfinalizer`不同的是：

1. 他可以注册多个终结函数。
2. 这些终结方法总是会被执行，无论在之前的`setup code`有没有抛出错误。这个方法对于正确关闭所有的fixture创建的资源非常便利，即使其一在创建或获取时失败：

    ```python
    @pytest.fixture
    def equipments(request):
        r = []
        for port in ('C1', 'C3', 'C28'):
            equip = connect(port)
            request.addfinalizer(equip.disconnect)
            r.append(equip)
        return r
    ```
在上面的例子中，如果`C28`抛出异常，那么`C1`和`C3`将会正确关闭。**当然，如果在终结函数注册之前就发生异常的话，这些是不会被执行的**。

**Fixtures can introspect the requesting test context, 就是在上下文的命名空间中会优先使用module namespace下的`smtpserver`。**如下面的例子。
```python
# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp = smtplib.SMTP(server)
    yield smtp
    print ("finalizing %s (%s)" % (smtp, server))
    smtp.close()
```
```python
# content of test_anothersmtp.py

smtpserver = "mail.python.org"  # will be read by smtp fixture

def test_showhelo(smtp):
    assert 0, smtp.helo()
```

# 5. 参数化的fixtures
fixture functions可以带入参数，依赖于这个fixture的一套测试会根据参数的不同运行多次。主要是协助一些部分做全面的功能测试，这些组成通常可以有多种配置。
延续上面的例子，我们可以标示这个fixture来创建两个`stmp`实例，这样会使所有使用这个fixture的测试运行两次。fixture function用过特殊的`request`对象来访问每个参数。
```python
# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module",
                params=["smtp.gmail.com", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param)
    yield smtp
    print ("finalizing %s" % smtp)
    smtp.close()
```
上面的改变是在@pytest.fixture装饰器中加入params，这个list中的每个值可以每次通过request.param访问。没有测试函数需要修改，但是却增加了不同配置下的测试情况。

pytest会为每个参数化下fixture的fixture value创建一个test ID（string），如上例中你会在测试结果中看到类似`test_ehlo[smtp.gmail.com]`和`test_ehlo[mail.python.org]`。这些ID可以配合-k标示来选择指定的情况运行，当一个失败时还是会标示出指定的情况。运行pytest加上`--collect-only`标示可以得到生成的ID。

Numbers, strings, booleans and None都常用的本身字符串来标示他们的test ID。其他的对象pytest会根据参数名字来创建。也可能自定义string来标示指定的fixture value，通过`ids`关键字参数实现：
```python
# content of test_ids.py
import pytest

@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param

def test_a(a):
    pass

def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None

@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param

def test_b(b):
    pass
```
上例展示了`ids`可以以list或者function的方式来运行的，都是以返回一个string来命名，下面是运行`--collect-only`来查看的结果，可以看到所有该目录下test相关的ID。其中`test_b[eggs]`是根据idfn返回的string来命名的ID，`test_b[1]`返回的是None，则根据传入的参数`1`来命名test ID。
```cmd
(bsawf) d:\git-checkout\learn-sth-everyday\Pytest>pytest --collect-only
============================= test session starts =============================
platform win32 -- Python 3.6.0, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: d:\git-checkout\learn-sth-everyday\Pytest, inifile:
collected 8 items
<Module 'test_ids.py'>
  <Function 'test_a[spam]'>
  <Function 'test_a[ham]'>
  <Function 'test_b[eggs]'>
  <Function 'test_b[1]'>
<Module 'test_params.py'>
  <Function 'test_ehlo[smtp.gmail.com]'>
  <Function 'test_noop[smtp.gmail.com]'>
  <Function 'test_ehlo[mail.python.org]'>
  <Function 'test_noop[mail.python.org]'>

======================== no tests ran in 0.07 seconds =========================
```

# 6. 模块化：将fixture用于其他的fixture function

fixtures不仅可以用于test functions，也能用于其他的fixtures本身。这对于fixtures的模块化设计和允许在不同项目中使用特定框架设定的fixtures非常有帮助。下面的例子中，通过传入另一文件中已经定义好的`smtp`资源来实例化一个`app`对象。
```python
# content of test_appsetup.py

import pytest

class App(object):
    def __init__(self, smtp):
        self.smtp = smtp

@pytest.fixture(scope="module")
def app(smtp):
    return App(smtp)

def test_smtp_exists(app):
    assert app.smtp
```
因为`smtp`使用了参数化，里面定义了params，所以这里的测试会用两个`App`的实例分别是两个单独的smtp server来执行两次测试。这里不需要`app`fixture直到`smtp`的参数设置，pytest会自动分析依赖关系。

**Note**，`app`和`smtp`的`scope`都是module。如果smtp是缓存在一个`session`的范围这个例子同样也能工作：fixtures调用一个更宽范围的fixtures是可以的但是其他的方式不行：一个session-scoped的fixture是不能以合理方式利用一个module-scoped的fixture。

```flow
st=>start: app(module)
op=>operation: use
e=>end: smtp(module/session)

st->op->e
```
# 7. 根据fixture实例自动分组测试

在测试运行期间，pytest会最小化激活的fixtures的数量。如果有一个参数化的fixture，则会用一个fixture实例运行所有的测试，在下一个fixture实例创建之前，finalizers（终结函数）会运行。除此之外，这样可以简化需要创建和使用全局状态的应用测试。
接下来的例子有两个参数化的fixture，其中一个是module-scoped，所有的functions都会用print来展示setup/teardown的流程：

```python
# content of test_module.py
import pytest

@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print ("  SETUP modarg %s" % param)
    yield param
    print ("  TEARDOWN modarg %s" % param)

@pytest.fixture(scope="function", params=[1,2])
def otherarg(request):
    param = request.param
    print ("  SETUP otherarg %s" % param)
    yield param
    print ("  TEARDOWN otherarg %s" % param)

def test_0(otherarg):
    print ("  RUN test0 with otherarg %s" % otherarg)
def test_1(modarg):
    print ("  RUN test1 with modarg %s" % modarg)
def test_2(otherarg, modarg):
    print ("  RUN test2 with otherarg %s and modarg %s" % (otherarg, modarg))
```
详尽模式运行：
```cmd
(bsawf) d:\git-checkout\learn-sth-everyday\Pytest>pytest -v -s test_module.py
============================= test session starts =============================
platform win32 -- Python 3.6.0, pytest-3.0.5, py-1.4.32, pluggy-0.4.0 -- d:\Anaconda3\python.exe
cachedir: .cache
rootdir: d:\git-checkout\learn-sth-everyday\Pytest, inifile:
collected 8 items

test_module.py::test_0[1]   SETUP otherarg 1
  RUN test0 with otherarg 1
PASSED  TEARDOWN otherarg 1

test_module.py::test_0[2]   SETUP otherarg 2
  RUN test0 with otherarg 2
PASSED  TEARDOWN otherarg 2

test_module.py::test_1[mod1]   SETUP modarg mod1
  RUN test1 with modarg mod1
PASSED
test_module.py::test_2[1-mod1]   SETUP otherarg 1
  RUN test2 with otherarg 1 and modarg mod1
PASSED  TEARDOWN otherarg 1

test_module.py::test_2[2-mod1]   SETUP otherarg 2
  RUN test2 with otherarg 2 and modarg mod1
PASSED  TEARDOWN otherarg 2

test_module.py::test_1[mod2]   TEARDOWN modarg mod1
  SETUP modarg mod2
  RUN test1 with modarg mod2
PASSED
test_module.py::test_2[1-mod2]   SETUP otherarg 1
  RUN test2 with otherarg 1 and modarg mod2
PASSED  TEARDOWN otherarg 1

test_module.py::test_2[2-mod2]   SETUP otherarg 2
  RUN test2 with otherarg 2 and modarg mod2
PASSED  TEARDOWN otherarg 2
  TEARDOWN modarg mod2


========================== 8 passed in 0.05 seconds ===========================
```
可以看到，module-scoped的`modarg`会对测试中几个可能激活的资源的测试顺序造成影响。`mod1`的finalizer是在`mod2`资源setup之前运行的。

特别地，test_0是完全独立且最先完成的测试。然后test_1在mod1下运行，接着test_2在mod1下运行，然后test_1在mod2下运行，最后test_2在mod2下运行。

# 8. 在classes，modules或者projects中使用fixtures

有时，测试函数是不直接访问一个fixture对象的。比如，测试需要用一个空的路径当作当前工作路径，但是并不关心当前的具体路径。下面的例子是用标准的[tempfile库](http://docs.python.org/library/tempfile.html)和pytest fixtures来实现的。我们将创建fixture的部分单独放到conftest.py中。
```python
# content of conftest.py

import pytest
import tempfile
import os

@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
```
通过`usefixtures`标志声明用处：
```python
# content of test_setenv.py
import os
import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit(object):
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
```
根据`usefixtures`标志，`cleandir`fixture会被每个test method运行时需要，就像你指定了一个"cleandir"函数参数给它们一样。运行并确认fixture被激活同时通过测试：（-q 是quiet模式）
```cmd
d:\git-checkout\learn-sth-everyday\Pytest>pytest -q test_setenv.py
..
2 passed in 0.05 seconds
```
你也能指定多个fixtures，像下面这样：
`@pytest.mark.usefixtures("cleandir", "anotherfixture")`
你也可以在test module的层级指定fixture的用途，通过使用标记机制的通用功能：
`pytestmark = pytest.mark.usefixtures("cleandir")`
**Note**，被指定的变量必须命名为`pytestmark`，比如像`foomark`这样的是不能激活fixtures的。

最后，你可以将你项目中所有测试都需要的fixtures放到一个ini-file中：
```init
# content of pytest.ini
[pytest]
usefixtures = cleandir
```

# 9. Auto use fixtures (xUnit setup on steroids)

偶尔地，我们可能希望在不明确声明一个函数参数或一个usefixtures装饰器的情况下，让fixtures被调用。以一个实际情况为例，假设我们有一个database fixture有begin/rollback/commit的结构，我们想要让每个测试方法都自动地跟随一个事务和回滚。下面是这个概念的一个虚拟的独立实现：
```python
# content of test_db_transact.py

import pytest

class DB(object):
    def __init__(self):
        self.intransaction = []
    def begin(self, name):
        self.intransaction.append(name)
    def rollback(self):
        self.intransaction.pop()

@pytest.fixture(scope="module")
def db():
    return DB()

class TestClass(object):
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        assert db.intransaction == ["test_method2"]
```
在class层级`transact`fixture被*autouse=True*标记，这个标记是为了实现，让这个class里面的所有测试方法，不需要在测试函数标记或class层级使用`usefixtures`装饰器的前提下就能使用这个fixture。

运行，得到两个测试通过：
```cmd
d:\git-checkout\learn-sth-everyday\Pytest>pytest -q test_db_transact.py
..
2 passed in 0.03 seconds
```
下面是autouse fixtures怎么在其他scope下工作的：

- autouse fixtures遵从`scope=`关键字参数：如果一个autouse fixture有`scope="session"`，不管它在哪里定义都只会运行一次。`scope='class'`表示将会在每个class运行一次等等。
- 如果一个autouse fixture在test module中定义，这个module中所有的测试函数将会自动使用它。
- 如果一个autouse fixture定义在conftest.py中，该路径下的所有测试module下的所有测试函数都会调用这个fixture。
- 最后，**请小心的使用：**如果你在插件中定义了一个autouse fixture，它将会在被安装的所有project的所有测试中调用。如果这个fixture无论如何都会在当前确定的settings下运行，比如在ini-file中，这样的设定非常有用。像这样一个全局的fixture应该快速确定它是否需要做任何工作，并避免不必要的imports或计算。

注意，上面的`transact`fixture同样也可以作为一个普通fixture，让它存在于项目中从而避免它广泛的激活。典型的实现方法是，将transact定义放到conftest.py中且不要使用`autouse`：
```python
# content of conftest.py
@pytest.fixture
def transact(self, request, db):
    db.begin()
    yield
    db.rollback()
```
然后通过声明需求来使用它：
```python
@pytest.mark.usefixtures("transact")
class TestClass(object):
    def test_method1(self):
        ...
```
所有TestClass中的测试函数将会用到transact fixture，但是其他的测试类或函数将不用调用，除非也声明了`transact`。

# 10. 移动fixturefunctions

如果你在实现测试的过程中发现一个fixture会用于多个测试，则可以将其移动到conftest.py中，或者甚至在不改变代码的情况下单独安装插件。fixture functions的查找顺序是test classes，test modules，conftest.py文件，最后是builtin和三方插件。

# 11. 从不同层级覆盖fixture（overriding）

在相对大型的测试套件中，你很有可能需要用本地的fixture来替换一个`global`或者`root`fixture，这样能保持代码的可读性和可维护性。
### 文件夹层级（conftest）覆盖一个fixture

给定测试文件结构：
```python
tests/
    __init__.py

    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def username():
            return 'username'

    test_something.py
        # content of tests/test_something.py
        def test_username(username):
            assert username == 'username'

    subfolder/
        __init__.py

        conftest.py
            # content of tests/subfolder/conftest.py
            import pytest

            @pytest.fixture
            def username(username):
                return 'overridden-' + username

        test_something.py
            # content of tests/subfolder/test_something.py
            def test_username(username):
                assert username == 'overridden-username'
```
如你所见，同名的fixture可以在某些文件层级上进行重写覆盖。注意，在上面的例子中，base或super fixture都能被覆盖的fixture轻松访问。

### 在test module层级覆盖
文件结构如下：
```python
tests/
    __init__.py

    conftest.py
        # content of tests/conftest.py
        @pytest.fixture
        def username():
            return 'username'

    test_something.py
        # content of tests/test_something.py
        import pytest

        @pytest.fixture
        def username(username):
            return 'overridden-' + username

        def test_username(username):
            assert username == 'overridden-username'

    test_something_else.py
        # content of tests/test_something_else.py
        import pytest

        @pytest.fixture
        def username(username):
            return 'overridden-else-' + username

        def test_username(username):
            assert username == 'overridden-else-username'
```
上面的例子中，conftest.py中定义的username fixture分别在某些具体的test module中被同名的fixture覆盖了，且这些覆盖的fixture依然可以调用最初的那个。

### 直接用测试参数来覆盖

文件结构如下：
```python
tests/
    __init__.py

    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def username():
            return 'username'

        @pytest.fixture
        def other_username(username):
            return 'other-' + username

    test_something.py
        # content of tests/test_something.py
        import pytest

        @pytest.mark.parametrize('username', ['directly-overridden-username'])
        def test_username(username):
            assert username == 'directly-overridden-username'

        @pytest.mark.parametrize('username', ['directly-overridden-username-other'])
        def test_username_other(other_username):
            assert other_username == 'other-directly-overridden-username-other'
```
在上例中，一个fixture的值被测试参数值给覆盖了。注意，在test_username_other这个测试函数中，即使没有直接使用`username`fixture，但是还是间接的被覆盖了。

### 用无参数化的fixture覆盖有的，反之亦然

给定文件结构如下：
```python
tests/
    __init__.py

    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture(params=['one', 'two', 'three'])
        def parametrized_username(request):
            return request.param

        @pytest.fixture
        def non_parametrized_username(request):
            return 'username'

    test_something.py
        # content of tests/test_something.py
        import pytest

        @pytest.fixture
        def parametrized_username():
            return 'overridden-username'

        @pytest.fixture(params=['one', 'two', 'three'])
        def non_parametrized_username(request):
            return request.param

        def test_username(parametrized_username):
            assert parametrized_username == 'overridden-username'

        def test_parametrized_username(non_parametrized_username):
            assert non_parametrized_username in ['one', 'two', 'three']

    test_something_else.py
        # content of tests/test_something_else.py
        def test_username(parametrized_username):
            assert parametrized_username in ['one', 'two', 'three']

        def test_username(non_parametrized_username):
            assert non_parametrized_username == 'username'
```
上面的例子中，在`test_something.py`中，一个参数化的fixture被无参数化的版本覆盖，另外一个fixture相反。test_something_else.py测试的是没有覆盖的情况。这样的覆盖操作同样适用于测试文件夹层级的。

