 <p align="center"><img src="/fig/itc.png" width="800" heigth="155"></p>

 # Programming Basics

 ### A introductory session for programming based data analysis

 ##### This session is designed for supporting the technical components of the course UPM_1: ***Planning Sustainable Cities (2020-1B)***, Department of Urban and Regional Planning and Geo-Information Management, Faculty Geo-Information Science and Earth Observation, University of Twente, Netherlands. Should you find the details of the course at https://canvas.utwente.nl/courses/6184.

 ##### Dr. Jiong (Jon) Wang,  j.wang-4@utwente.nl


 ## Foreword
 -------------------
 One of the most important skills in urban planning and management is **problem solving**. **Problem solving** is the ability to formulate problems and find solutions. For example, to analyze sustainable urban development, you may want to formulate one of the problems as *“How to quantify urban sustainability?”*, and your solutions include *find relevant indicators and combine them reasonably*. It turns out that learning to program is the best way to practice your problem-solving skills. Although there are many tools and software products can support processing indicators and multi-criteria analysis, programming allows you to handle your data and methodology with the greatest flexibility, where you benefit from your creativity. **If you did NOT but would like to know how to start programming, then this page for you.**

 Obviously, it is impossible to cover every aspect of programming within a session designed for only one day. But it *is possible* to introduce you some of the basic elements that computer scientists are working with every day. Hence, you will be able to think like a computer scientist, and build sophisticated programs based upon your knowledge about these basic elements. The good news is that, you will get yourself familiar with different data types and see how programs can handle the data flexibly, you will even be able to define simple functions to automatically complete tasks for you, and apply your own functions to real spatial datasets!

 To ensure that you can immediately benefit from those largest programming communities, we will start to learn programming by using *Python*, one of the most popular high level programming language today. While using *python*, you need to keep in mind that your purpose is to capture the feeling about programming, instead of just learning *Python*. In the following content, we will walk through some of the basic elements and features that lead you to define your own functions. You will apply the learnt skills to accomplish two challenges. Specifically, you will see:

 - 0. Values, variables and naming conventions
 - 1. Expressions
 - 2. Functions
 - 3. Conditionals
 - 4. Iteration
 - 5. Extended data types
 - 6. Reading and writing files
 - 7. Visualization
 - 8. Challenge 1: working with point datasets
 - 9. Challenge 2: working with raster datasets

 There can be quite a steep learning curve while you walk through the content, so please alway keep in mind that it is very impornt and efficient to get hands on experience while learning programming. DO NOT just sit back and read the codes, DO modify and rewrite, and check the difference.

 ##### Credit
 -------------------
 You're very welcome to use the content of this page for teaching and learning. Credit to this work can be given as:
 ~~~
 J. Wang, Programming Basics: A introductory session for programming based data analysis (2020), GitHub repository,
 https://github.com/wonjohn/Bayes_for_Regression
 ~~~

 Apart from the two **Challenges**, the contents on this page is largely based upon Allen Downey's book:
 ~~~
 Downey, A.B., Brooks Jr, F.P., Peek, J., Todino, G., Strang, J., Robbins, A., Lamb, L., Hannah, E., Joy, W., Horton, M. and Cameron, D., 2012. Think Python 2e. Green Tea Press.
 ~~~
 which is publicly accessible as an open material at: http://greenteapress.com/thinkpython2/thinkpython2.pdf.

 The data used in the **Challenges** is from research project operated by Dr. Lu, Meng with details at:
 ~~~
 Lu, M., Schmitz, O., de Hoogh, K., Kai, Q. and Karssenberg, D., 2020. Evaluation of different methods and data sources to optimise modelling of NO2 at a global scale. Environment international, 142, p.105856.
 ~~~

 ## Getting started
 -------------------
 We will be deploy this course by taking advantage of cloud based resources. The *Python* codes written in *Jupyter Notebook* will be loaded into *Google Colab*, which is an online programming interface working exactly like *Jupyter Notebook* in your browser. So you can simply treat it as an online version of Jupyter Notebook, the only difference is that your code will be executed on the server provided by *Google* in the cloud.

 Before going to *Colab*, you need a *Google/Gmail* account. Once you create and login in *Colab* with your account, you will immediately see an interface below in your browser:

 <p align="center"><img src="/fig/0.png" width="800" heigth="450"></p>

 On this page, you can familiarize yourself with the panels of the main menu, the table of contents and programming/coding cells. You will be mainly working in the panel of programming/coding cells, where you can write either *Python* codes or texts in each cell.

 In order to work with codes I prepared for you, you can simply **open** the notebook in this *GitHub* repository by providing the link to *Colab*. Click **File** > **Open notebook**, you will see dialogue box below:

 <p align="center"><img src="/fig/1.png" width="800" heigth="450"></p>

 Copy and paste the address of this *GitHub* repository at *https://github.com/jonwangio/Programming-Basics*, and hit **enter**, you will find the *Jupyter Notebook* listed. **Double click** to select the listed notebook, you are now totally set with your programming environment! As you can see sections prepared for you shown below:

 <p align="center"><img src="/fig/2.png" width="800" heigth="450"></p>

 <p align="center"><img src="/fig/3.png" width="800" heigth="450"></p>

 <p align="center"><img src="/fig/4.png" width="800" heigth="450"></p>

 As been said, feel free to modify, delete, and add the programs to get the most out of your hands-on experience. Enjoy programming!
