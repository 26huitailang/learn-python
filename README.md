#Hello World

# Commit msg format

## AngularJS规范

header，body，footer

- revert如果有，如commit revert了其他commit，那么**header**应该以“revert:”开始，后面跟上被revert的commit标题。body应该是This reverts commit <hash\>
- header，包括type，分隔符，主题
    - type：
        - feat(feature)
        - fix(bug fix)
        - docs(documentation)
        - style(formating, missing semi colons, ...)
        - refactor
        - test(when adding missing tests)
        - chore(maintain)
        主题信息能够简短描述commit即可，结尾不要用"."，开头不要大写。使用祈使语态，如change，而不是changed。
- msg body，为什么做这个commit，以及改动前后的对比
- footer
    - breaking changes：重要改动声明。
    - referencing issues：如果和issue相关，指出来。

**example**
```
fix($compile): couple of unit tests for IE9

Older IEs serialize html uppercased, but IE9 does not...
Would be better to expect case insensitive, unfortunately jasmine does
not allow to user regexps for throw expectations.

Closes #392
Breaks foo.bar api, foo.baz should be used instead
```
## thoughtbot 规范

[地址](https://github.com/thoughtbot/dotfiles/blob/master/gitmessage)
```
# 50-character subject line
#
# 72-character wrapped longer description. This should answer:
#
# * Why was this change necessary?
# * How does it address the problem?
# * Are there any side effects?
#
# Include a link to the ticket, if any.
```

关于这个规范更详细的说明可以参考他们的一篇文章 5 Useful Tips For A Better Commit Message 。简单来说：

1. 第一行不超过 50 个字符
2. 第二行空一行
3. 第三行开始是描述信息，每行长度不超过 72 个字符，超过了自己换行。
4. 描述信息主要说明：
    a. 这个改动为什么是必要的？
    b. 这个改动解决了什么问题？
    c. 会影响到哪些其他的代码？
5. 最后最好有一个相应 ticket 的链接

---
Here are some bacis knowledge with links:
* [how to use git by liaoxuefeng](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374385852170d9c7adf13c30429b9660d0eb689dd43a000)

* [how to use github](https://guides.github.com/activities/hello-world/)

* [what the rules of Markdown in github](https://guides.github.com/features/mastering-markdown/)

* [regular-expression](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000#0)

---
# _Files Included_

## AngularJS Learn
- Official-tutorial
- [W3CSchool](http://www.w3cschool.cn/angularjs/angularjs-controllers.html)

## Beginning-Python-2nd-Edition
- Project1-Instant-Markup

## Learn-python-the-hard-way

##liaoxuefeng tutorial

## practice
- LeetCodeOJ
- SPOJ-basics
- others

## pythonchallenge
- [pythonchallenge](http://www.pythonchallenge.com/)



