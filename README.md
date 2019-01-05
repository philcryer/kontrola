# kontrola

_/kɔnˈtrɔ.la/ - inspection (the act of examining something, often closely) [Polish]_ (<a href="https://commons.wikimedia.org/wiki/File:Pl-kontrola.ogg?embedplayer=yes">audio</a>) 

A script that uses nmap to sweep a subnet looking for ports with SSL certs, then querying those certs to discover upcoming expiration dates. Besides discovery, it can also do more traditional tracking using a host based file that you provide. See usage for an example configuration.

## Motivation

There are plenty of scripts out there that will check SSL/TLS certificates and let you know when they're due for renewal, but none (that I've found) that can optionally sweep a subnet, finding live hosts with ports presenting SSL certifcates, and then querying those certificates for their expiration dates, and finally displaying themm in a easy to read manner online.

## Features

* scans a static list of hosts for SSL certificate expiration dates (default)
* bulids a simple, easy to read report in html using [Bootstrap](https://getbootstrap.com), listing all Expired, Expiring, and Valid certifcate dates
* (optional) uses [nmap](https://nmap.org) to discover live hosts on a subnet, either the on the script is running on, or a targeted one
* (optional) pokes at live hosts, checking known TLS/SSL ports to see if they are available

## Report screenshots

The html report is built using [Bootstrap](http://getbootstrap.com/), written to the `html/` directory by default, and is straightforward in its presentation

<div align="center"><img src="src/screenshot.png" border="1" alt="Screenshot"></div>

## Usage

* Checkout the code

```
git clone https://github.com/philcryer/kontrola.git
cd kontrola
```

### Host list mode (default)

* Edit any varables in the script, if desired
* Edit the `domains.txt` file, adding domains you want be checked
* Run the script

```
./kontrola
```

Check the `html/` directory for the output report

### Portscan mode

* Run the script, with discovery turned on
* By default it will seach the `/32` of the subnet the host is running on 

```
discovery="yes" ./kontrola 
```

* Optionally you can list a subnet target for it to sweep

```
discovery="yes" discovery_subnet="10.10.0.0/32" ./kontrola 
```

## Todo

(Possible) upcoming features

* switches so you can run `kontrola -d` to do discovery, instead of setting the variable and running it
* find a javascript plugin to allow for searching of found hostnames
* provide an easy to parse csv output file, alongside the html output
* generate a PDF report with red/yellow/green icons showing what is due/expired
* email alerts, or at least have an email option `kontrola -e` to have the report emailed (again, PDF would be better for this than the html out)

#### As always, pull requests welcome!

## Acknoldegements

Like most (all?) good software, `kontrola` builds off of other excellent open source projects. At first I was using scripts I found on GitHub, that were excellent, but didn't do all of what I wanted. I integrated some ideas from the following projects. If `kontrola` doesn't do what you need, look at these as options

* [ssl-cert-check](https://github.com/Matty9191/ssl-cert-check)
* [checkssl](https://github.com/srvrco/checkssl)
* [go-check-certs](https://github.com/timewasted/go-check-certs)

Other outstanding open source projects used to build, presesnt, and search the reports

* [nmap](https://nmap.org/) a security scanner used to discover live hosts and query network ports
* [Bootstrap](http://getbootstrap.com/) a front-end component library that is used to build the html reports
* [Tipue Search](http://www.tipue.com/search/) a jQuery-based site search plugin for the genearted html reports

## License

MIT License

Copyright (c) 2019 Phil Cryer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Thanks
