# IFCHybrid Import Options Class

Source: https://www.revitapidocs.com/2026/29e2dd13-9b70-29f1-3ff7-9058e67972bd.htm

---

| IFCHybrid Import Options Class |
| --- |

A set of options to decide on extra AnyCAD processing. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.IFC IFCHybridImportOptions 
  
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class IFCHybridImportOptions : IDisposable
```

```
Public Class IFCHybridImportOptions
	Implements IDisposable
```

```
public ref class IFCHybridImportOptions : IDisposable
```

```
type IFCHybridImportOptions = 
    class
        interface IDisposable
    end
```
The IFCHybridImportOptions type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HybridGrids](IFCHybrid-Import-Options-Hybrid-Grids-Property.md) | True if we should use AnyCAD to process grids, false otherwise. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HybridLevels](IFCHybrid-Import-Options-Hybrid-Levels-Property.md) | True if we should use AnyCAD to process levels, false otherwise. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HybridPropertySets](IFCHybrid-Import-Options-Hybrid-Property-Sets-Property.md) | True if we should use AnyCAD to process property sets, false otherwise. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](IFCHybrid-Import-Options-Is-Valid-Object-Property.md) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Create](IFCHybrid-Import-Options-Create-Method.md) | Create a IFCHybridImportOptions from an options string, or null if it isn't hybrid mode. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](IFCHybrid-Import-Options-Dispose-Method.md) | Releases all resources used by the IFCHybridImportOptions |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [ToString(IFCHybridImportOptions)](IFCHybrid-Import-Options-To-String-IFCHybrid-Import-Options-Method.md) | Converts the IFCHybridImportOptions class to a revit.ini\-compatible string. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
