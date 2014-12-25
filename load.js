"use strict";
var http = require('http'),
    fs = require('fs');
function get_url() {
    if (!('i' in get_url))
        get_url.i = 1;
    return ['http://androidweekly.net/issues/issue-', get_url.i++];
}

function request() {
    var data = [];
    var url = get_url();
    var i = url[1];
    url = url.join('');

    var req = http.get(url, function(res) {
        console.log(url + '\t' + res.statusCode);
        res
            .on('data', function collect(d) {
                data.push(d.toString('utf8'));
            })
            .on('end', function() {
                data = data.join('');
                data = data.replace(/>[\s]*</mg, '><').trim();
                fs.writeFileSync('loads/' + i + '.html', data);
                if (200 == res.statusCode)
                    request();
            });
    })
        .on('error', function(e) {
            console.log("Got error: " + e.message);
        });
    req.end();
    return req;
}

for(var i=0; i<3; i++)
    setTimeout(request, i * 2000);

