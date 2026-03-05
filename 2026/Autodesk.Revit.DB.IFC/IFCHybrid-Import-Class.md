# IFCHybrid Import Class

Source: https://www.revitapidocs.com/2026/7f0506a4-c093-7f4b-e2d0-07df141f4767.htm

---

| IFCHybrid Import Class |
| --- |

Driver for Performing Hybrid Imports. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.IFC IFCHybridImport 
  
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class IFCHybridImport : IDisposable
```

```
Public Class IFCHybridImport
	Implements IDisposable
```

```
public ref class IFCHybridImport : IDisposable
```

```
type IFCHybridImport = 
    class
        interface IDisposable
    end
```
The IFCHybridImport type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IFCHybridImport](c2391e7e-063b-6739-c090-60994fc64a01.htm) | Constructs a new IFCHybridImport instance for importing IFC via Hybrid method. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](e0eb98ed-a5e7-0bba-25b9-59a2a21a947a.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateMap](42b95227-2e47-e5a5-91a6-cee54975e818.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](cc567ee4-1f34-6853-3062-3d4aafdacec4.htm) | Releases all resources used by the IFCHybridImport |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetIFCStepIdToElementIdMap](ea1bb754-dfb1-5dea-7eee-a584f3406b79.htm) | Retrieves the association between the original IFC STEP identifiers and the created or updated Elements. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ImportElements(Document, String)](IFCHybrid-Import-Import-Elements-Document-String-Method.md) | **Obsolete.** Imports IFC Elements using AnyCAD. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ImportElements(Document, String, IFCHybridImportOptions)](IFCHybrid-Import-Import-Elements-Document-String-IFCHybrid-Import-Options-Method.md) | Imports IFC Elements using AnyCAD. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [UpdateElements(Document, String)](IFCHybrid-Import-Update-Elements-Document-String-Method.md) | **Obsolete.** Updates IFC Elements using AnyCAD. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [UpdateElements(Document, String, IFCHybridImportOptions)](IFCHybrid-Import-Update-Elements-Document-String-IFCHybrid-Import-Options-Method.md) | Updates IFC Elements using AnyCAD. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)
