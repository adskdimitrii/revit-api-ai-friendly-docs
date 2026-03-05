# IFCHybrid Import Options Create Method

Source: https://www.revitapidocs.com/2026/9f65726a-8aea-cbd3-4884-752c73d318e9.htm

---

| IFCHybrid Import Options Create Method |
| --- |

Create a IFCHybridImportOptions from an options string, or null if it isn't hybrid mode. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IFCHybridImportOptions Create(
	string optionString
)
```

```
Public Shared Function Create ( 
	optionString As String
) As IFCHybridImportOptions
```

```
public:
static IFCHybridImportOptions^ Create(
	String^ optionString
)
```

```
static member Create : 
        optionString : string -> IFCHybridImportOptions 
```

#### Parameters

optionString String
:   The options string.

#### Return Value

[IFCHybridImportOptions](IFCHybrid-Import-Options-Class.md) 
The IFCHybridImportOptions, or null. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCHybridImportOptions Class](IFCHybrid-Import-Options-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
