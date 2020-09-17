import allure


@allure.step('第一步输入用户名')
def input_name():
    pass


@allure.step('第二步输入密码')
def input_pwd():
    pass


@allure.step('第三步登录成功')
def click_login():
    pass


def login_success():
    input_name()
    input_pwd()
    click_login()


@allure.title('测试用例登录')
@allure.feature('测试登录功能')
@allure.story('正向测试用例')
@allure.severity('blocker')
def test_logs():
    """登录成功"""
    login_success()
    assert 1


@allure.feature('测试下订单功能')
@allure.story('对小米手机进行下订单')
@allure.severity('trivial')
@allure.title('小米')
@allure.description_html('<H1>谁tm买小米A</H1>')
def test_order():
    # 把附件追缴到allure报告中
    with open(r'mtxhomework\allrue.jpg', 'rb') as f:
        con = f.read()
    allure.attach(con, '上传了一张图片', allure.attachment_type.JPG)
    assert 1


@allure.title('测试链接的展示效果')
@allure.feature('测试链接展示效果')
@allure.description('测试的是链接没有实际意义')
@allure.link('https://www.baidu.com/', name='link')
@allure.issue('https://www.cnblogs.com/lovehuange/',name='禅道链接')
@allure.testcase("http://momentjs.cn/", name='测试失败Erro')
def test_url():
    pass
