# IFCHybrid Import Options To String(IFCHybrid Import Options) Method

Source: https://www.revitapidocs.com/2026/1c26061d-bc28-981e-156c-fb3f8f81f14a.htm

---

| IFCHybrid Import Options To String(IFCHybrid Import Options) Method |
| --- |

Converts the IFCHybridImportOptions class to a revit.ini\-compatible string. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string ToString(
	IFCHybridImportOptions options
)
```

```
Public Shared Function ToString ( 
	options As IFCHybridImportOptions
) As String
```

```
public:
static String^ ToString(
	IFCHybridImportOptions^ options
)
```

```
static member ToString : 
        options : IFCHybridImportOptions -> string 
```

#### Parameters

options [IFCHybridImportOptions](IFCHybrid-Import-Options-Class.md)
:   The optional IFCHybridImportOptions class.

#### Return Value

String 
The options string. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A null IFCHybridImportOptions will assume that this is a legacy import. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCHybridImportOptions Class](IFCHybrid-Import-Options-Class.md) [ToString Overload](IFCHybrid-Import-Options-To-String-Method.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
