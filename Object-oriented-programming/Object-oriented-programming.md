# python 物件導向資料收集心得

- 物件導向 **object-oriented programming** 可以幫助程式工程師，在開發軟體時，提升過撐性與維護性

- OOP  按照程式的內容進行分類，建立不同的類別 (class)，利用定義後的類別實例化後建立物件(object)

- **class** 基本架構
  
  - 一個類別 class 可包含以下三個項目(包含一種即可)
    
    - 屬性 (Attribute)
      
      - 存放物件內的資料，一般會在屬性前面加上 `self` 代表實例化物件的參考，表示目前的物件，也就是告訴 Class 目前是在設定那一個物件的屬性
    
    - 建構式 (Constructor)
      
      - 建立物件時會自動執行的**Method**(方法)
      
      - 常見的是`def __init__(self, [SOME/PARAMETER])` ，在物件實例化時，負責初始化物件內的屬性
    
    - 方法 (Method)


