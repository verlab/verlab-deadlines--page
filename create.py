#!/usr/bin/env python

import yaml

with open("_data/conferences.yml", 'r') as stream:
    conferencesdata = yaml.load(stream)

conferencesdata = sorted(conferencesdata, key=lambda k: k['deadline'])


html = '''<div id="conf_id" class=" conf_sub-conf ">
  <div class="row">
      <div class="col-xs-12 col-sm-6">
          <a href="conf_link"><b>conf_name conf_year</b></a>
          <div class="meta">
            conf_data // <a href="http://maps.google.com/?q=conf_place">conf_place</a>
          </div>
      </div>
      <div class="col-xs-12 col-sm-6">
        <span class="timer"></span>
        <div class="deadline">
          <div>Deadline:
            <span class="deadline-time"></span>
          </div>
        </div>
      </div>
  </div>
  <hr>
</div>


'''


javascript = '''// adjust date according to deadline timezone
var timezone =  "America/New_York" ;
var confDate = moment.tz("conf_deadline", timezone);

// render countdown timer
$('#conf_id .timer').countdown(confDate.toDate(), function(event) {
  $(this).html(event.strftime('%D days %Hh %Mm %Ss'));
});
$('#conf_id .deadline-time').html(confDate.toString());

// check if date has passed, add 'past' class to it
var today = moment();
if (today.diff(confDate) > 0)
$('#conf_id').addClass('past');


'''


allconferences_html = '''
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title>AI Conference Deadlines</title>
    <meta name="description" content="Countdowns to top CV/NLP/ML/Robotics/AI conference deadlines">
    <meta name="author" content="Abhishek Das">
    <link rel="stylesheet" type="text/css" href="static/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="static/css/deadlines.css" media="screen,projection">
    <link rel="shortcut icon" href="static/img/favicon.png">
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script type="text/javascript" src="static/js/jquery.countdown.min.js"></script>
    <script src="static/js/moment.min.js"></script>
    <script src="static/js/moment-timezone-with-data.min.js"></script>
    <script src="static/js/store.min.js"></script>

  </head>
  <body>
    <div class="top-strip"></div>
    <div class="container">
        <div class="page-header">
            <div class="row">
                <div class="col-xs-12 col-sm-8">
                  <h1>
                    VeRLab Conference Deadlines
                  </h1>
                </div>
                <div class="meta col-xs-12">
                  Countdowns to VeRLab conference deadlines
                 
                </div>
            </div>
            <br>
            <div class="row">
              <div class="col-xs-12">
                <!-- <div class="well"> -->
                  <form class="form-horizontal">
                    <div class="form-group">
                      
                      <div class="col-md-2 col-xs-5">
                        <div class="checkbox">
                          <label>
                            <input type="checkbox" id="ML-checkbox" class=""> Machine Learning
                          </label>
                        </div>
                      </div>
                      
                      <div class="col-md-2 col-xs-5">
                        <div class="checkbox">
                          <label>
                            <input type="checkbox" id="CV-checkbox" class=""> Computer Vision
                          </label>
                        </div>
                      </div>
                      
                      <div class="col-md-2 col-xs-5">
                        <div class="checkbox">
                          <label>
                            <input type="checkbox" id="NLP-checkbox" class=""> Natural Language Processing
                          </label>
                        </div>
                      </div>
                      
                      <div class="col-md-2 col-xs-5">
                        <div class="checkbox">
                          <label>
                            <input type="checkbox" id="RO-checkbox" class=""> Robotics
                          </label>
                        </div>
                      </div>
                      
                      <div class="col-md-2 col-xs-5">
                        <div class="checkbox">
                          <label>
                            <input type="checkbox" id="SP-checkbox" class=""> Speech/SigProc
                          </label>
                        </div>
                      </div>
                      
                    </div>
                  </form>
                <!-- </div> -->
              </div>
            </div>
        </div>



'''


allconferences_javascript = '''
    <script type="text/javascript" charset="utf-8">
    $(function() {
'''

for conf in conferencesdata:
	confenrence_str = html
	confenrence_str = confenrence_str.replace('conf_id', conf['id'])
	confenrence_str = confenrence_str.replace('conf_link', conf['link'])
	confenrence_str = confenrence_str.replace('conf_name', conf['name'])
	confenrence_str = confenrence_str.replace('conf_year', str(conf['year']))
	confenrence_str = confenrence_str.replace('conf_place', conf['place'])
	confenrence_str = confenrence_str.replace('conf_sub', conf['sub'])
	confenrence_str = confenrence_str.replace('conf_data', conf['date'])
	


	allconferences_html += confenrence_str


	javascript_str = javascript
	javascript_str = javascript_str.replace('conf_id', conf['id'])
	javascript_str = javascript_str.replace('conf_deadline', conf['deadline'])
	
	allconferences_javascript += javascript_str


allconferences_html += '''

    <footer>
      Maintained by VeRLab. Based on https://aideadlin.es created by Abhishek Das
    </footer>
    <hr>
</div>
'''

allconferences_javascript+= '''

        // Set checkboxes
        var conf_type_data = [{"name":"Machine Learning","sub":"ML"},{"name":"Computer Vision","sub":"CV"},{"name":"Natural Language Processing","sub":"NLP"},{"name":"Robotics","sub":"RO"},{"name":"Speech/SigProc","sub":"SP"}];
        var all_subs = [];
        for (var i = 0; i < conf_type_data.length; i++) {
          all_subs[i] = conf_type_data[i]['sub'];
        }
        var subs = store.get('aideadlin.es');
        if (subs === undefined) {
          subs = all_subs;
          for (var i = 0; i < subs.length; i++) {
            $('#' + subs[i] + '-checkbox').prop('checked', true);
          }
        } else {
          for (var i = 0; i < subs.length; i++) {
            $('#' + subs[i] + '-checkbox').prop('checked', true);
          }
        }
        // Hide unchecked subs
        for (var i = 0; i < all_subs.length; i++) {
          if (subs.indexOf(all_subs[i]) < 0) {
            $('.' + all_subs[i] + '-conf').hide();
          }
        }
        store.set('aideadlin.es', subs);

        // Event handler on checkbox change
        $('form :checkbox').change(function(e) {
          var checked = $(this).is(':checked');
          var cid = $(this).prop('id');
          var csub = cid.substring(0, cid.length - 9);
          if (checked == true) {
            $('.' + csub + '-conf').show();
            if (subs.indexOf(csub) < 0)
              subs.push(csub);
          }
          else {
            $('.' + csub + '-conf').hide();
            var idx = subs.indexOf(csub);
            if (idx >= 0)
              subs.splice(idx, 1);
          }
          console.log(subs);
          store.set('aideadlin.es', subs);
        });
    });
    <!-- Google analytics -->
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
      ga('create', 'UA-36274081-2', 'auto');
      ga('send', 'pageview');
    </script>
'''

allconferences_html = allconferences_html + allconferences_javascript

allconferences_html += '''
  </body>
</html>
'''


print(allconferences_html)
