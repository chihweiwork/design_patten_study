# python 物件導向資料收集心得

- 物件導向 **object-oriented programming** 可以幫助程式工程師，在開發軟體時，提升過撐性與維護性

- OOP  按照程式的內容進行分類，建立不同的類別 (class)，利用定義後的類別實例化後建立物件(object)

- **class** 的命名方式
  
  - 一般使用 **Pascal** 命名方法：
    
    - 駝峰名法：
      
      - 小駝峰式命名法：
        
        `myFirstTestClass`
      
      - 大駝峰式命名法：
        
        `MyFirstTestClass`

- **class** 基本架構
  
  - 一個類別 class 可包含以下三個項目(包含一種即可)
    
    - 屬性 (Attribute)
      
      - 存放物件內的資料，一般會在屬性前面加上 `self` 代表實例化物件的參考，表示目前的物件，也就是告訴 Class 目前是在設定那一個物件的屬性
    
    - 建構式 (Constructor)
      
      - 建立物件時會自動執行的**Method**(方法)
      
      - 常見的是`def __init__(self, [SOME/PARAMETER])` ，在物件實例化時，負責初始化物件內的屬性
    
    - 方法 (Method)
      
      - 定義物件的行為，與 **function** 的語法很像，不過與建構是相同，必須包含一個 **self** 
  
  - 整合上述三點，簡單的 class 定義的方式如下：
    
    - ```python
      class MyClass：#定義類別的名稱
          def __init__(self, par1, par2): #建構式 (Constructor)
              """
              基本的建構式，內如必須包含一個 self，
              可以在這裡初始化 class 的屬性，如下所示：
              """
              self.par1 = par1 # class 的屬性
              self.par2 = par2 # class 的屬性
          def my_method(self, par3): #定義 mathod 的方法 
              """
              在這裡定義 mathod 的內容，其中必須包含 self，
              也可以傳入變數進入 method 中，如 par3
              """
              self.par4 = par3 + 1 # method 的內容
                                   # self.par4 在變數前加上 self
                                   # 可以讓變數在 class 中都可以使用
      if __name__ == "__main__":
          """
          建立一個 my_class 是 MyClass 類別(class) 的物件 (object)
          也可以稱為實例化一個 MyClass 的物件
          """
          my_class = MyClass("AA", "BB") 
          """
          使用 method 的方法
          """
          my_class.my_method(100)
          
      ```
  
  - 設定屬性的方法有三種：
    
    - ```python
      class ThreeWaysSettingAttribute:
          # 第一種：定義在 __init__ 外面
          my_name = "chihwei"
          def __init__(self):
              # 第二種：定義在 __init__ 中
              self.my_name = "chihwei"
      
      if __name__ == "__main__":
          # 實例化 class
          test_class = ThreeWaysSettingAttribute()
          # 第三種：定義屬性的方法：
          test_class.my_name = "chihwei"
      ```
