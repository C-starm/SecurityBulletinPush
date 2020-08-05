import android
import apple
import wechat

if __name__ == '__main__':
    apple = apple.do()
    android = android.do()
    # You need input your token
    token = ""
    wechat.do(token=token, apple=apple, android=android)
