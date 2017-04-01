// 任何来自于网页并且包括来自 evaluate() 内部代码的控制台信息，默认不会显示。
// var url = 'http://baidu.com';
// var page = require('webpage').create();
// page.open(url, function (status) {
//     var title = page.evaluate(function () {
//         return document.title;
//     });
//     console.log('Page title is ' + title);
//     phantom.exit()
// });

//需要重写这个行为，使用 onConsoleMessage 回调函数，示例可以改写成
var url = 'http://baidu.com';
var page = require('webpage').create();
page.onConsoleMessage = function (msg) {
    console.log(msg);
};
page.open(url, function (status) {
    page.evaluate(function () {
        console.log(document.title);
    });
    phantom.exit();
});
