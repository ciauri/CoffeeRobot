import random
insultsList = ["Do they sell men's clothes where you bought your shirt?","You suck.","3 inches isn't average bro \n-Dr.E Linstead","If you were any fatter, you'd eat hay and shit in the street! \n-Dr.E Linstead to class","You look like a before picture.","You look like you should be selling chickens on the side of the road.","Idiot.","Kevin works harder than you.","Go get hit by a train.","Nice face!","How's your sister? ;)","Have a nice day!"]

def updateCoffeeSite(coffeeReady):
    if(coffeeReady):
        target = open("public.html", 'w')
        target.write("""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                          <title>Team Pi-Rate's Coffee Updater</title>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1">
                          <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
                          <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
                          <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
                          <style>
 
  			    .fade {
			    padding:20px;
			    color: white;
 			    opacity: .1;
  			    transition: opacity .25s ease-in-out;
 			    -moz-transition: opacity .25s ease-in-out;
 			    -webkit-transition: opacity .25s ease-in-out;
 			    }
			  
 			    .fade:hover {
 			    opacity: 1;
  			    }

                            html {
                              height: 100%;
                            }

                            body {
                        background: #49311C; /* For browsers that do not support gradients */
                            background: -webkit-linear-gradient(red, yellow); /* For Safari 5.1 to 6.0 */
                            background: -o-linear-gradient(red, yellow); /* For Opera 11.1 to 12.0 */
                            background: -moz-linear-gradient(red, yellow); /* For Firefox 3.6 to 15 */
                            background: linear-gradient(#49311C, black); /* Standard syntax */
                        height: 100%;
                            margin: 0;
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                            }

                            #coffeeHeader {
                              margin-top: 35vh;
                              color: white;
                            }
                            /* Remove the navbar's default margin-bottom and rounded borders */ 
                            .navbar {
                              margin-bottom: 0;
                              border-radius: 0;
                            }
                            
                            /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
                            .row.content {height: 450px}
                            
                            /* Set black background color, white text and some padding */
                            footer {
                              background-color: black;
                              color: white;
                              padding: 15px;
                            }
                            
                            /* On small screens, set height to 'auto' for sidenav and grid */
                            @media screen and (max-width: 767px) {
                              .sidenav {
                                height: auto;
                                padding: 15px;
                              }
                              .row.content {height:auto;} 
                            }
                          </style>
                        </head>
                        <body>
                          
                        <div class="container-fluid text-center">    
                          <div class="row content">
                            <div class="col-sm-10  col-sm-offset-1 text-center"> 
                              <h1 id="coffeeHeader">Is The Coffee Ready?</h1>
                              <h3 style="color:white;">Yep.</h3>
			      <p class="fade">""" +random.choice(insultsList) + """</p>
                            </div>
                        </div>

                        <footer class="container-fluid text-center navbar-fixed-bottom">
                          <p>Team Pi-Rates &copy; 2016</p>
                        </footer>

                        </body>
                        </html>""")
    else:
        target = open("public.html", 'w')
        target.write("""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                          <title>Team Pi-Rate's Coffee Updater</title>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1">
                          <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
                          <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
                          <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
                          <style>
 
  			    .fade {
			    padding:20px;
			    color: white;
 			    opacity: .1;
  			    transition: opacity .25s ease-in-out;
 			    -moz-transition: opacity .25s ease-in-out;
 			    -webkit-transition: opacity .25s ease-in-out;
 			    }
			  
 			    .fade:hover {
 			    opacity: 1;
  			    }

                            html {
                              height: 100%;
                            }

                            body {
                        background: #49311C; /* For browsers that do not support gradients */
                            background: -webkit-linear-gradient(red, yellow); /* For Safari 5.1 to 6.0 */
                            background: -o-linear-gradient(red, yellow); /* For Opera 11.1 to 12.0 */
                            background: -moz-linear-gradient(red, yellow); /* For Firefox 3.6 to 15 */
                            background: linear-gradient(#49311C, black); /* Standard syntax */
                        height: 100%;
                            margin: 0;
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                            }

                            #coffeeHeader {
                              margin-top: 35vh;
                              color: white;
                            }
                            /* Remove the navbar's default margin-bottom and rounded borders */ 
                            .navbar {
                              margin-bottom: 0;
                              border-radius: 0;
                            }
                            
                            /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
                            .row.content {height: 450px}
                            
                            /* Set black background color, white text and some padding */
                            footer {
                              background-color: black;
                              color: white;
                              padding: 15px;
                            }
                            
                            /* On small screens, set height to 'auto' for sidenav and grid */
                            @media screen and (max-width: 767px) {
                              .sidenav {
                                height: auto;
                                padding: 15px;
                              }
                              .row.content {height:auto;} 
                            }
                          </style>
                        </head>
                        <body>
                          
                        <div class="container-fluid text-center">    
                          <div class="row content">
                            <div class="col-sm-10  col-sm-offset-1 text-center"> 
                              <h1 id="coffeeHeader">Is The Coffee Ready?</h1>
                              <h3 style="color:white;">Nope.</h3>
			      <p class="fade">""" +random.choice(insultsList) + """</p>
                            </div>
                        </div>

                        <footer class="container-fluid text-center navbar-fixed-bottom">
                          <p>Team Pi-Rates &copy; 2016</p>
                        </footer>

                        </body>
                        </html>""")

