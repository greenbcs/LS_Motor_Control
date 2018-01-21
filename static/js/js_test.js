function button_click1() {
    // 第一个动机的按钮
    var device = document.getElementById("device1");
    device.onclick = function () {
        var button_display = document.getElementById("button_display1");
        if (button_display.style.display=='block'){
            button_display.style.display = 'none';
        }
        else{
            button_display.style.display = 'block';
        }
    };
}

function button_click2() {
    // 第二个动机的按钮
    var device = document.getElementById("device2");
    device.onclick = function () {
        var button_display = document.getElementById("button_display2");
        if (button_display.style.display=='block'){
            button_display.style.display = 'none';
        }
        else{
            button_display.style.display = 'block';
        }
    };
}

function button_click3() {
    // 第三个动机的按钮
    var device = document.getElementById("device3");
    device.onclick = function () {
        var button_display = document.getElementById("button_display3");
        if (button_display.style.display=='block'){
            button_display.style.display = 'none';
        }
        else{
            button_display.style.display = 'block';
        }
    };
}

function button_click4() {
    // 第三个动机的按钮
    var device = document.getElementById("device4");
    device.onclick = function () {
        var button_display = document.getElementById("button_display4");
        if (button_display.style.display=='block'){
            button_display.style.display = 'none';
        }
        else{
            button_display.style.display = 'block';
        }
    };
}

function button_click5() {
    // 第五个动机的按钮
    var device = document.getElementById("device5");
    device.onclick = function () {
        var button_display = document.getElementById("button_display5");
        if (button_display.style.display=='block'){
            button_display.style.display = 'none';
        }
        else{
            button_display.style.display = 'block';
        }
    };
}

// 执行绑定函数的函数
function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function() {
            oldonload();
            func();
        }
    }
}

addLoadEvent(button_click1);
addLoadEvent(button_click2);
addLoadEvent(button_click3);
addLoadEvent(button_click4);
addLoadEvent(button_click5);