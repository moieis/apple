import time
from pywebio.output import *
from pywebio.session import *
from pywebio.platform import *
from pywebio_battery import *
from selenium import webdriver
import base64
from selenium.webdriver.common.by import By
import os
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import argparse


ss = open('stl.css','r').read()
sss= open('pal.png','rb').read()
yu = open('yemen.png','rb').read()

app = Flask(__name__)



def inputt0():
    ######################################### getting the driver ready ################################
    with use_scope(name='screen', clear=True):
        put_html('''<div id="container">
                        <div id="monitor">
                          <div id="monitorscreen">

    <div class="table center">
      <div class="monitor-wrapper center">
        <div class="monitor center">
          <p> !! يرجى  الانتظار   ثواني !!</p>
        </div>
      </div>
    </div>

                           <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                            </div>
                        </div>
                      </div>''')
    set_localstorage(key='next_0', value='NoValue')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    # put_text("done")

    driver.get("https://zefoy.com/")
    with use_scope(name='screen', clear=True):
                put_html('''<div id="container">
                            <div id="monitor">
                              <div id="monitorscreen">

        <div class="table center">
          <div class="monitor-wrapper center">
            <div class="monitor center">
              <p> !! يتم الان تجهيز المشغل لن يستغرق سواء ثواني معدودة !!</p>
            </div>
          </div>
        </div>

                               <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                </div>
                            </div>
                          </div>''')
    time.sleep(5)

    def one_time():
                set_localstorage(key='next_0', value='NoValue')
                ################################  input  0  ################################
                try:
                    shot = driver.find_element(By.XPATH,
                                               '/html/body/div[5]/div[2]/form/div/div')  # code imput and screenshot #############
                    shot.screenshot('foo.png')


                except:
                    driver.save_screenshot('foo.png')
                try:
                        txt_shot = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input')
                except:
                        pass
                with use_scope(name='screen', clear=True):
                    with open('foo.png', 'rb') as image_file:
                        image_data = base64.b64encode(image_file.read()).decode('utf-8')
                    image_html = f'''
            
                                          <div id="container">
                             <div id="monitor">
                               <div id="monitorscreen">
                                  <img  class='d' src="data:image/jpeg;base64,{image_data}" alt="Image" style="max-width: 100%; height: auto;">
            
                               </div>
                             </div>
                           </div>
            
            
                           '''

                    # JavaScript code to set the image's src attribute
                    js_code = f'''
                                              <script>
                                                  document.getElementById('monitorscreen').innerHTML = '{image_html}';
                                              </script>
                                          '''

                    # Display the HTML and execute the JavaScript
                    put_html(image_html + js_code)
                time.sleep(2)

                with use_scope(name='doit', clear=True):
                    put_html('''  
            
                                                                           <p class='username'><b>ادخل الكلمة التي في الشاشة هنا :  </b></p>
            
            
                                                              <div>
                                                      <input type="text" id="form" placeholder="!   هنا !">
                                                      <input class='btz' type="submit" id="button" value="Enter">
                                                  </div>
            
                                                  <!-- Modal for displaying values -->
                                                  <div id="myModal" class="modal">
                                                      <div class="modal-content">
                                                          <h2>? هل انت متاكد من هذه المعلومات </h2>
                                                          <h2 class='dsd'> الكلمة التي في الشاشة : <span id="modalUsername"></span></h4>
            
                                                          <button id="confirmButton">نعم التالي</button>
                                                          <button id="editButton">تعديل</button>
                                                      </div>
                                                  </div>
                                              <script>
                                                  // Function to move focus to the next input or button on "Enter" key press
                                                  function moveToNextInput(event, currentInput, nextInput) {
                                                      if (event.key === "Enter") {
                                                          event.preventDefault();
                                                          nextInput.focus();
                                                      }
                                                  }
            
                                                  // Add event listeners for moving focus on "Enter" key press
            
            
                                                  document.getElementById("form").addEventListener("keypress", function (event) {
                                                      moveToNextInput(event, this, document.getElementById("button"));
                                                  });
            
                                                  // Add click event listener to the button to open the modal
                                                  document.getElementById("button").addEventListener("click", function () {
                                                      // Get the values from the input fields
                                                      var username = document.getElementById("form").value;
            
                                                      // Display values in the modal
                                                      document.getElementById("modalUsername").textContent = username;
            
                                                      // Show the modal
                                                      var modal = document.getElementById("myModal");
                                                      modal.style.display = "block";
            
                                                      // Add click event listener to the confirm button
                                                      document.getElementById("confirmButton").addEventListener("click", function () {
                                                          // Store the values in local storage
                                                          localStorage.setItem("username", username);
                                                          localStorage.setItem("next_0", "1");
            
                                                          // Close the modal
                                                          modal.style.display = "none";
                                                      });
            
                                                      // Add click event listener to the edit button
                                                      document.getElementById("editButton").addEventListener("click", function () {
                                                          // Close the modal
                                                          modal.style.display = "none";
                                                      });
                                                  });
            
                                                  // Close the modal if the user clicks outside of it
                                                  window.onclick = function (event) {
                                                      var modal = document.getElementById("myModal");
                                                      if (event.target === modal) {
                                                          modal.style.display = "none";
                                                      }
                                                  };
                                              </script>
                                              ''')
            #############################################chack @###############################
                while True:
                    chack = get_localstorage(key='next_0')
                    if chack == '1':
                        clear('doit')
                        with use_scope(name='screen', clear=True):
                            put_html('''<div id="container">
                          <div id="monitor">
                            <div id="monitorscreen">
                             <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                            </div>
                          </div>
                        </div>''')
                        txt_shot.send_keys(get_localstorage('username'))
                        time.sleep(2)
                        click_shot = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/div/button')
                        click_shot.click()
                        time.sleep(6)
                        search_text = "Captcha code is incorrect."  # Replace with the text you want to search for

                        # Find all elements that contain the search_text
                        elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{search_text}')]")
                        if elements:
                            for element in elements:
                                element_xpath = driver.execute_script(
                                    "function getXPath(element) { " +
                                    "    if (element.id !== '')" +
                                    "        return 'id(\"' + element.id + '\")';" +
                                    "    if (element === document.body)" +
                                    "        return element.tagName.toLowerCase();" +
                                    "    var ix = 1;" +
                                    "    var siblings = element.parentNode.childNodes;" +
                                    "    for (var i = 0; i < siblings.length; i++) {" +
                                    "        var sibling = siblings[i];" +
                                    "        if (sibling === element) {" +
                                    "            return getXPath(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + ix + ']';" +
                                    "        }" +
                                    "        if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {" +
                                    "            ix++;" +
                                    "        }" +
                                    "    }" +
                                    "}"
                                    "return getXPath(arguments[0]);", element)

                                toast('الكلمة التي ادخلتها خاطائة الرجاء المحاولة مرة اخرى', color='error')
                                driver.refresh()
                                one_time()


                        else:

                            with use_scope(name='screen', clear=True):
                                put_html('''<div id="container">
                              <div id="monitor">
                                <div id="monitorscreen">
                                 <div class="success-animation">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" /><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" /></svg>
            </div>
                                </div>
                              </div>
                            </div>''')
                            clear(scope='doit')
                            break

                inputt1(driver)

    one_time()




def inputt1(driver):
    set_localstorage(key='next_1', value='NoValue')
    ####################################input1################################
    with use_scope(name='screen', clear=True):
        put_html('''<div id="container">
                        <div id="monitor">
                          <div id="monitorscreen">

    <div class="table center">
      <div class="monitor-wrapper center">
        <div class="monitor center">
          <p> !!  ✅ تاكد من ان الحساب مفتوح وان الرابط يعمل بشكل صحيح !!</p>
        </div>
      </div>
    </div>

                           <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                            </div>
                        </div>
                      </div>''')
    with use_scope(name='doit', clear=True):
        put_html('''  

                                                <p class='username'><b>اسم المستخدم :  </b></p>

                                                <p class='videolink'><b>  رابط الفيد :  </b></p>
                                   <div>
                           <input type="text" id="form" placeholder="! ضع اسم المستخدم هنا !">
                           <input type="text" id="formv" placeholder="! ضع رابط الفيد هنا !">
                           <input type="submit" id="button" value="Enter">
                       </div>

                       <!-- Modal for displaying values -->
                       <div id="myModal" class="modal">
                           <div class="modal-content">
                               <h2>? هل انت متاكد من هذه المعلومات </h2>
                               <h4 class='dsd'>اسم المستخدم : <span id="modalUsername"></span></h4>
                               <h4  class='dsd'>رابط الفيد  : <span id="modalVideoLink"></span></h4>
                               <button id="confirmButton">نعم التالي</button>
                               <button id="editButton">تعديل</button>
                           </div>
                       </div>
                   <script>
                       // Function to move focus to the next input or button on "Enter" key press
                       function moveToNextInput(event, currentInput, nextInput) {
                           if (event.key === "Enter") {
                               event.preventDefault();
                               nextInput.focus();
                           }
                       }

                       // Add event listeners for moving focus on "Enter" key press
                       document.getElementById("form").addEventListener("keypress", function (event) {
                           moveToNextInput(event, this, document.getElementById("formv"));
                       });

                       document.getElementById("formv").addEventListener("keypress", function (event) {
                           moveToNextInput(event, this, document.getElementById("button"));
                       });

                       // Add click event listener to the button to open the modal
                       document.getElementById("button").addEventListener("click", function () {
                           // Get the values from the input fields
                           var username = document.getElementById("form").value;
                           var videoLink = document.getElementById("formv").value;

                           // Display values in the modal
                           document.getElementById("modalUsername").textContent = username;
                           document.getElementById("modalVideoLink").textContent = videoLink;

                           // Show the modal
                           var modal = document.getElementById("myModal");
                           modal.style.display = "block";

                           // Add click event listener to the confirm button
                           document.getElementById("confirmButton").addEventListener("click", function () {
                               // Store the values in local storage
                               localStorage.setItem("username", username);
                               localStorage.setItem("videoLink", videoLink);
                               localStorage.setItem("next_1", "1");

                               // Close the modal
                               modal.style.display = "none";
                           });

                           // Add click event listener to the edit button
                           document.getElementById("editButton").addEventListener("click", function () {
                               // Close the modal
                               modal.style.display = "none";
                           });
                       });

                       // Close the modal if the user clicks outside of it
                       window.onclick = function (event) {
                           var modal = document.getElementById("myModal");
                           if (event.target === modal) {
                               modal.style.display = "none";
                           }
                       };
                   </script>
                   ''')

    while True:
        chack = get_localstorage(key='next_1')
        if chack == '1':
            clear(scope='doit')
            break
    ########################################## Start doing ##################################################
    opation = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[4]/div/button')
    # /html/body/div[6]/div/div[2]/div/div/div[5]/div/button viewss

    opation.click()

    time.sleep(6)

    link = driver.find_element(By.XPATH, '/html/body/div[9]/div/form/div/input')
    time.sleep(2)
    link_get = get_localstorage(key='videoLink')
    userget= get_localstorage(key='username')
    link.send_keys(link_get)

    time.sleep(3)
    ########################################################################################

    click_ve = driver.find_element(By.XPATH, '/html/body/div[9]/div/form/div/div/button')
    click_ve.click()


    search_text = 'Please enter valid video URL.'





    try:
        time.sleep(3)
        with use_scope(name='screen', clear=True):
            put_html(f'''<div id="container">
                             <div id="monitor">
                               <div id="monitorscreen">

         <div class="table center">
           <div class="monitor-wrapper center">
             <div class="monitor center">
               <p> يتم الان التحقق من رابط الفيديو ......</p>
             </div>
           </div>
         </div>

                                <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                 </div>
                             </div>
                           </div>''')
        chackkurl = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/span').text
        try:
            chackwait = driver.find_element(By.XPATH,'/html/body/div[9]/div/div/span[1]').text
        except:
            pass
        if chackkurl in ['Please enter valid video URL.']:
            with use_scope(name='screen', clear=True):
                put_html('''<div id="container">
                                <div id="monitor">
                                  <div id="monitorscreen">

            <div class="table center">
              <div class="monitor-wrapper center">
                <div class="monitor center">
                  <p> 🛑❌الرابط غير صالح او ان الحساب مقفل❌🛑 </p>
                </div>
              </div>
            </div>

                                   <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                    </div>
                                </div>
                              </div>''')

            time.sleep(3)
            with use_scope(name='screen', clear=True):
                put_html('''<div id="container">
                                <div id="monitor">
                                  <div id="monitorscreen">

            <div class="table center">
              <div class="monitor-wrapper center">
                <div class="monitor center">
                  <p> 🛑 سوف يتم تحويلك تلقائيا انتظر لحظة  ِ🛑  </p>
                </div>
              </div>
            </div>

                                   <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                    </div>
                                </div>
                              </div>''')

            time.sleep(3)
            driver.back()
            inputt1(driver)

        elif chackwait.split(' ')[0] in ['Please'] or chackwait.split(' ')[1] in ['wait']:
            with use_scope(name='screen', clear=True):
                put_html('''<div id="container">
                                                    <div id="monitor">
                                                      <div id="monitorscreen">

                                <div class="table center">
                                  <div class="monitor-wrapper center">
                                    <div class="monitor center">
                                      <p> ! مدة الانتظار اقل من دقيقة للتم العملية بنجاح انتظر  </p>
                                    </div>
                                  </div>
                                </div>

                                                       <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                                        </div>
                                                    </div>
                                                  </div>''')
        else:
            time.sleep(2)
            with use_scope(name='screen', clear=True):
                    put_html('''<div id="container">
                                                    <div id="monitor">
                                                      <div id="monitorscreen">
        
                                <div class="table center">
                                  <div class="monitor-wrapper center">
                                    <div class="monitor center">
                                      <p> ! وجدنا الفيديو سنقوم بسحب التعليقات انتضر لحظة  </p>
                                    </div>
                                  </div>
                                </div>
        
                                                       <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                                        </div>
                                                    </div>
                                                  </div>''')
                    pass

    except:
        with use_scope(name='screen', clear=True):
            put_html('''<div id="container">
                            <div id="monitor">
                              <div id="monitorscreen">

        <div class="table center">
          <div class="monitor-wrapper center">
            <div class="monitor center">
              <p> 🛑hereeeeeeeeeeeeeeeeeeeeee❌🛑 </p>
            </div>
          </div>
        </div>

                               <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                </div>
                            </div>
                          </div>''')

        # time.sleep(3)
        #
        #
        # time.sleep(3)
        # driver.back()
        # inputt1(driver)


                        # with use_scope(name='screen', clear=True):
                        #     with open('comcount.png', 'rb') as image_file:
                        #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
                        #     image_html = f'''
                        #
                        #                           <div id="container">
                        #              <div id="monitor">
                        #                <div id="monitorscreen">
                        #                   <img  class='d' src="data:image/jpeg;base64,{image_data}" alt="Image" style="max-width: 100%; height: auto;">
                        #
                        #                </div>
                        #              </div>
                        #            </div>
                        #
                        #
                        #            '''
                        #
                        #     # JavaScript code to set the image's src attribute
                        #     js_code = f'''
                        #                               <script>
                        #                                   document.getElementById('monitorscreen').innerHTML = '{image_html}';
                        #                               </script>
                        #                           '''
                        #
                        #     # Display the HTML and execute the JavaScript
                        #     put_html(image_html + js_code)
                        # count_com = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[1]/div/form/button').text
                        #
                        # if int(count_com) > 500:
                        #     with use_scope(name='screen', clear=True):
                        #         put_html(f'''<div id="container">
                        #                         <div id="monitor">
                        #                           <div id="monitorscreen">
                        #
                        #     <div class="table center">
                        #       <div class="monitor-wrapper center">
                        #         <div class="monitor center">
                        #           <p> 🛑 يظهر تعليق اي دعم يمكنك لاتقلق ٥٠٠ من اكثر العدد تعليقك يظهر لا ان الممكن من 🛑 </p>
                        #         </div>
                        #       </div>
                        #     </div>
                        #      <p> {count_com} </p>
                        #
                        #                            <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                        #                             </div>
                        #                         </div>
                        #                       </div>''')



    try:
        commant=driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[1]/div/form/button').text

        with use_scope(name='screen', clear=True):
                put_html(f'''<div id="container">
                                <div id="monitor">
                                  <div id="monitorscreen">

            <div class="table center">
              <div class="monitor-wrapper center">
                <div class="monitor center">
                  <p>    عدد التعليقات المتوفرة حاليا   {commant} </p>
                </div>
              </div>
            </div>
                        <div class="success-animation">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" /><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" /></svg>
            </div>
                                  
                                  
                                     </div>
                                </div>
                              </div>''')

                time.sleep(3)

    except:
        toast('عدد التعليقات غير متوفر حاليا',color='error')



    try:







                    #/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[3]
                    #
                    with use_scope(name='screen', clear=True):
                        put_html('''<div id="container">
                                        <div id="monitor">
                                          <div id="monitorscreen">

                    <div class="table center">
                      <div class="monitor-wrapper center">
                        <div class="monitor center">
                          <p> 🛑 جاري البحث على تعليقك من بين التعليقات  ِ🛑  </p>
                        </div>
                      </div>
                    </div>

                                           <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                            </div>
                                        </div>
                                      </div>''')
                    for w in range(2):

                        for p in range(0, 8):
                            try:
                                if userget[0] in ['@','user:',' ']:
                                        search_text = f"{userget}"  # Replace with the text you want to search for


                                else:
                                    search_text = f"@{userget}"  # Replace with the text you want to search for

                                # Find all elements that contain the search_text
                                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{search_text}')]")
                                if elements:
                                    for element in elements:
                                        element_xpath = driver.execute_script(
                                            "function getXPath(element) { " +
                                            "    if (element.id !== '')" +
                                            "        return 'id(\"' + element.id + '\")';" +
                                            "    if (element === document.body)" +
                                            "        return element.tagName.toLowerCase();" +
                                            "    var ix = 1;" +
                                            "    var siblings = element.parentNode.childNodes;" +
                                            "    for (var i = 0; i < siblings.length; i++) {" +
                                            "        var sibling = siblings[i];" +
                                            "        if (sibling === element) {" +
                                            "            return getXPath(element.parentNode) + '/' + element.tagName.toLowerCase() + '[' + ix + ']';" +
                                            "        }" +
                                            "        if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {" +
                                            "            ix++;" +
                                            "        }" +
                                            "    }" +
                                            "}"
                                            "return getXPath(arguments[0]);", element)

                                        xpathh = element_xpath.split('/')[1].split('m')[1]
                                        time.sleep(3)
                                        try:

                                            driver.find_element(By.XPATH, '/html/body/div[9]/div/form/div/div/button').click()

                                        except:
                                            pass

                                        time.sleep(6)

                                        with use_scope(name='screen', clear=True):
                                            put_html('''<div id="container">
                                                            <div id="monitor">
                                                              <div id="monitorscreen">

                                        <div class="table center">
                                          <div class="monitor-wrapper center">
                                            <div class="monitor center">
                                              <p> 🛑!!!!! من الممكن ان لايظهر تعليقك اذا تم اضافته حديثاً او عدد التعليقات اكثر من ٥٠٠ !!!!!! ِ🛑  </p>
                                            </div>
                                          </div>
                                        </div>

                                                               <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                                                </div>
                                                            </div>
                                                          </div>''')
                                        try:
                                            driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[1]/div/form/button').click()

                                            time.sleep(6)

                                            driver.find_element(By.XPATH,
                                                                f'/html/body/div[9]/div/div/form{xpathh}/ul/li/div/button').click()
                                        except:
                                            pass


                                        #####heree#####heree#####heree#####heree#####heree#####heree#####heree

                                        value = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/span[1]').text
                                        value_1 = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/span').text

                                        with use_scope(name='screen', clear=True):
                                            put_html('''<div id="container">
                                                                                         <div id="monitor">
                                                                                           <div id="monitorscreen">
                                                                                            <div class="success-animation">
                                                                       <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" /><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" /></svg>
                                                                       </div>
                                                                       <div class="table center">
                                                               <div class="monitor-wrapper center">
                                                                 <div class="monitor center">
                                                                   <p>✅ تم ارسال ١٠٠ لايك بنجاح ✅ </p>
                                                                 </div>
                                                               </div>
                                                             </div>
 <div class="success-animation">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" /><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" /></svg>
            </div>

                                                                                           </div>
                                                                                         </div>
                                                                                       </div>''')

                                        time.sleep(4)
                                        with use_scope(name='screen', clear=True):
                                            put_html(f'''<div id="container">
                                                                                 <div id="monitor">
                                                                                   <div id="monitorscreen">

                                                             <div class="table center">
                                                               <div class="monitor-wrapper center">
                                                                 <div class="monitor center">
                                                                   <p> {value} </p>
                                                                 </div>
                                                               </div>
                                                             </div>

                                                                                   <div class="success-animation">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" /><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" /></svg>
            </div> </div>
                                                                                 </div>
                                                                               </div>''')



                                        #####heree#####heree#####heree#####heree#####heree#####heree#####heree








                                else:

                                    time.sleep(5)
                                    try:
                                        driver.find_element(By.XPATH, f'/html/body/div[9]/div/div/div[1]/div/form[{p}]/button').click()
                                    except:

                                        #########expt of#########
                                        pass
                                    time.sleep(5)

                            except:
                                driver.find_element(By.XPATH, f'/html/body/div[9]/div/form/div/div/button').click()
                                time.sleep(5)

                                pass

                        ########################## for 1 sec ###################################################

                        driver.find_element(By.XPATH, f'/html/body/div[9]/div/div/div[1]/div/form[1]/button').click()

                        ########################## for 1 sec ###################################################




    except:

                with use_scope(name='screen', clear=True):
                    put_html('''<div id="container">
                                    <div id="monitor">
                                      <div id="monitorscreen">
                
                <div class="table center">
                  <div class="monitor-wrapper center">
                    <div class="monitor center">
                      <p> 🛑❌الرابط غير صالح او ان الحساب مقفل❌🛑 </p>
                    </div>
                  </div>
                </div>
                
                                       <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                        </div>
                                    </div>
                                  </div>''')

                time.sleep(3)
                with use_scope(name='screen', clear=True):
                    put_html('''<div id="container">
                                    <div id="monitor">
                                      <div id="monitorscreen">
                
                <div class="table center">
                  <div class="monitor-wrapper center">
                    <div class="monitor center">
                      <p> 🛑 سوف يتم تحويلك تلقائيا انتظر لحظة  ِ🛑  </p>
                    </div>
                  </div>
                </div>
                
                                       <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
                                        </div>
                                    </div>
                                  </div>''')

                time.sleep(3)
                driver.back()
                inputt1(driver)


config(title='Free 🇵🇸',css_style=f'''{ss}''',js_code='''''')

def intro():

               set_env(output_max_width='100%')

               ############ RESET THE LOCALHOST VAR ########################
               set_localstorage(key='next_0', value='NoValue')
               set_localstorage(key='next_1',value='NoValue')
               #############################################################
               put_html('''
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Flag-map_of_Yemen.png" class="yemenimage">
    ''')

               put_html('''
                       <img src="https://imageupload.io/ib/S1MkuBeGeWH05cR_1697670226.png" class="logoimage">
                   ''')


               put_html('''
                       <img src= 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Flag_map_of_Mandatory_Palestine_with_a_Palestinian_flag.svg' class="plimage">
                   ''')

















               put_text(''' وَلَقَدْ كَتَبْنَا فِي الزَّبُورِ مِن بَعْدِ الذِّكْرِ أَنَّ الْأَرْضَ يَرِثُهَا عِبَادِيَ الصَّالِحُونَ''')

               with use_scope(name='screen', clear=True):



                           with open('pal.png', 'rb') as image_file:
                               image_data = base64.b64encode(image_file.read()).decode('utf-8')
                           image_html = f'''
                           
                           <div id="container">
              <div id="monitor">
                <div id="monitorscreen">
                   <img  class='d' src="data:image/jpeg;base64,{image_data}" alt="Image" style="max-width: 100%; height: auto;">
            
                </div>
              </div>
            </div>
                           
                        
            '''

                           # JavaScript code to set the image's src attribute
                           js_code = f'''
                               <script>
                                   document.getElementById('monitorscreen').innerHTML = '{image_html}';
                               </script>
                           '''

                           # Display the HTML and execute the JavaScript
                           put_html(image_html + js_code)







               time.sleep(1) # this is the next pic screen
               with use_scope(name='screen', clear=True):
                   with open('foo.png', 'rb') as image_file:
                       image_data = base64.b64encode(image_file.read()).decode('utf-8')
                   image_html = f'''

                                         <div id="container">
                            <div id="monitor">
                              <div id="monitorscreen">
                                 <img  class='d' src="data:image/jpeg;base64,{image_data}" alt="Image" style="max-width: 100%; height: auto;">

                              </div>
                            </div>
                          </div>


                          '''

                   # JavaScript code to set the image's src attribute
                   js_code = f'''
                                             <script>
                                                 document.getElementById('monitorscreen').innerHTML = '{image_html}';
                                             </script>
                                         '''

                   # Display the HTML and execute the JavaScript
                   put_html(image_html + js_code)

               def gg():
                   with use_scope('popp',clear=True):
                         put_html('''



                   <div id="popupContainer" class="popup-container">
                       <div class="frame">
                           <!-- Your existing HTML content goes here -->



                   <div class="frame">
                     <div class="panel">
                       <div class="header flex">

                   			<span class="title">التعليمات</span>
                   		</div>

                   		<div class="notifications clearfix">
                   			<div class="line"></div>
                   			<div class="notification">
                   				<div class="circle"></div>
                   				<span class="time">الخطوة الاولى</span>
                   				<p class='formm'><b>  ضع التعليق :</b>  قم بنشر أرائك في اي فيديو على  التيكتوك </p>
                   			</div>
                   			<div class="notification">
                   				<div class="circle"></div>
                   				<span class="time">الخظوة الثالثة</span>
                   				<p class='formm'><b> اسم المستخدم :</b> ادخل اسم المستخدم الخاص بك بشكل صحيح في التيك توك</p>
                   			</div>
                   			<div class="notification">
                   				<div class="circle"></div>
                   				<span class="time">الخطوة الثانية</span>
                   				<p class='formm'><b>عنوان الفيديو  : \n</b>  قم بنسخ رابط فديو التيكتوك  الذي علقت عليه واللصقة هنا</p>
                   			</div>
                   			<div class="notification">
                   				<div class="circle"></div>
                   				<span class="time">الخطوة الثانية</span>
                   				<p class='formm'><b>تتم المعالجة  : \n</b>  سوف تتم المعالجة ويتم البحث على تعليقك واستهدافة بحزمة الدعم الالكتروني </p>
                   			</div>
                   			<div class="notification">
                   				<div class="circle"></div>
                   				<span class="time">الخطوة الثانية</span>
                   				<p class='formm'><b>حزمة الدعم الالكتروني  : \n</b> هي عبارة عن اتمته لدعم تعليقك بحيث يحصل كل تعليق على ٨٠ الى ١٢٠ اعجاب كل ثلاث دقائق في التشغيل </p>
                   			</div>
                   			<div class="notification">
                   				<div class="circle"></div>
                   				<span class="time">الخطوة الثانية</span>
                   				<p class='formm'><b>هاااااااام : \n</b> نحن نرى ان ذو الصوت يجب ان يصل صوتة لذلك قمنا بهذا الاتمتة ليتم سماع صوتك ومشاهدته وجعل تعليقك في اول مسار التعليقات ويمكن ان يصل الى ١٠ الف لايك اذا قمت ب التتبعية وسيظهر للمعنيين يرجى ملاحظة ان اذا لم يتم العثور على تعليقك فبسبب كمية التعليقات وايضا ننصح بالانتظار نصف الى ساعة بعد التعليق وقبل الاتمتة لنستصيع العثور علية بشكل اسرع !   </p>
                   			</div>



                   		</div>
                     </div>




                   </div>

                    </div>
                       <button id="closePopupButton"  class="realshinmark" >Close Popup</button>

                   </div>
                   <script>
                    function openPopup() {
                           document.getElementById('popupContainer').style.display = 'flex';
                       }

                       document.getElementById('closePopupButton').addEventListener('click', function() {
                           document.getElementById('popupContainer').style.display = 'none';
                       });

                   </script>''')

               put_html('''
               
               
                 <button onclick="openPopup()" id="openPopupButton" class="Btn">اضغط للتعليمات 
     <svg fill="#000000" version="1.1" class= 'svg' xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="15px" height="18px" viewBox="0 0 45.311 45.311" xml:space="preserve"><g stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g> <g> <path d="M22.675,0.02c-0.006,0-0.014,0.001-0.02,0.001c-0.007,0-0.013-0.001-0.02-0.001C10.135,0.02,0,10.154,0,22.656 c0,12.5,10.135,22.635,22.635,22.635c0.007,0,0.013,0,0.02,0c0.006,0,0.014,0,0.02,0c12.5,0,22.635-10.135,22.635-22.635 C45.311,10.154,35.176,0.02,22.675,0.02z M22.675,38.811c-0.006,0-0.014-0.001-0.02-0.001c-0.007,0-0.013,0.001-0.02,0.001 c-2.046,0-3.705-1.658-3.705-3.705c0-2.045,1.659-3.703,3.705-3.703c0.007,0,0.013,0,0.02,0c0.006,0,0.014,0,0.02,0 c2.045,0,3.706,1.658,3.706,3.703C26.381,37.152,24.723,38.811,22.675,38.811z M27.988,10.578 c-0.242,3.697-1.932,14.692-1.932,14.692c0,1.854-1.519,3.356-3.373,3.356c-0.01,0-0.02,0-0.029,0c-0.009,0-0.02,0-0.029,0 c-1.853,0-3.372-1.504-3.372-3.356c0,0-1.689-10.995-1.931-14.692C17.202,8.727,18.62,5.29,22.626,5.29 c0.01,0,0.02,0.001,0.029,0.001c0.009,0,0.019-0.001,0.029-0.001C26.689,5.29,28.109,8.727,27.988,10.578z"></path> </g> </g></svg>
    </button>
''').onclick(gg)

               with use_scope(name='screen', clear=True):
                   put_html('''<div id="containerr">
                    <div id="monitorr">
                      <div id="monitorscreenn">
                       <a class="btn-shine" > صوتك = بصمتك   </a>
                         </div>
                    </div>
                  </div>''')
               time.sleep(3)
               with use_scope(name='screen', clear=True):
                   put_html('''<div id="containerr">
                    <div id="monitorr">
                      <div id="monitorscreenn">
                       <a class="btn-shine" >سنمنحك صلاحية ايصال صوتك  </a>
                         </div>
                    </div>
                  </div>''')
               time.sleep(3)
               with use_scope(name='screen', clear=True):
                   put_html('''<div id="containerr">
                    <div id="monitorr">
                      <div id="monitorscreenn">
                       <a class="btn-shine" >  وباجتهادك سوف يكون في اعلى الفديوهات</a>
                         </div>
                    </div>
                  </div>''')
               time.sleep(3)
               with use_scope(name='screen', clear=True):
                   put_html('''<div id="containerr">
                     <div id="monitorr">
                       <div id="monitorscreenn">
                        <a class="btn-shine" >  مع كل تعليق ٨٠-١٠٠ اعجاب</a>
                          </div>
                     </div>
                   </div>''')

               time.sleep(4)

               with use_scope(name='screen', clear=True):
                   put_html('''<div id="containerr">
                      <div id="monitorr">
                        <div id="monitorscreenn">
                         <a class="btn-shine" >نخلي مسؤوليتنا امام الله وامامكم لاي استخدام غير مشروع</a>
                           </div>
                      </div>
                    </div>''')

               time.sleep(4)

               with use_scope(name='screen', clear=True):
                   put_html('''<div id="containerr">
                                     <div id="monitorr">
                                       <div id="monitorscreenn">
                                        <a class="btn-shine" >! اتبع التعليمات لتفهم </a>
                                          </div>
                                     </div>
                                   </div>''')

               time.sleep(3)






               inputt0()





app.add_url_rule('/tool', 'webio_view', webio_view(intro),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(intro, port=args.port,debug=True,cdn=True)









