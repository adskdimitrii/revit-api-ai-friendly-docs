# Export IFCCategory Info Class

Source: https://www.revitapidocs.com/2026/5da998a3-e973-3b76-5f5d-ed4769fef46e.htm

---

| Export IFCCategory Info Class |
| --- |

Represents the mapped IFC information stored in the template. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB ExportIFCCategoryInfo 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class ExportIFCCategoryInfo : IDisposable
```

```
Public Class ExportIFCCategoryInfo
	Implements IDisposable
```

```
public ref class ExportIFCCategoryInfo : IDisposable
```

```
type ExportIFCCategoryInfo = 
    class
        interface IDisposable
    end
```
The ExportIFCCategoryInfo type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ExportIFCCategoryInfo](c40c1a56-a7c5-f118-d227-008de235ab93.htm) | Constructs a new ExportIFCCategoryInfo with default values. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ExportIFCCategoryInfo(Boolean, String, String, String, String)](6d71a690-b014-7dc2-7e65-9c20627e56f5.htm) | Constructs a new ExportIFCCategoryInfo with input values. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IFCEntityName](e281d55a-fb5b-708e-c35a-23986476c35d.htm) | The name of the IFC entity mapped to a particular Revit category. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IFCExportFlag](Export-IFCCategory-Info-IFCExport-Flag-Property.md) | The boolean value that indicates whether the category is exported to IFC. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IFCPredefinedType](36813915-9d3d-4a67-c8c4-d6eef3a6b116.htm) | The name of the predefined type mapped to a particular Revit category. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IFCPresentationLayerName](30927b9a-2bb8-fe2b-dd53-f3f9dfe6bb5e.htm) | The name of the presentation layer mapped to a particular Revit category. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IFCUserDefinedType](022d165c-b9ea-4773-96a1-25db30f0bca2.htm) | The name of the user\-defined type mapped to a particular Revit category. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](c79967df-2263-94ca-01a7-7392f1f2a2e6.htm) | Specifies whether the .NET object represents a valid Revit entity. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](2dbd5489-e1e3-6f1e-927b-3bcc1c1522ad.htm) | Releases all resources used by the ExportIFCCategoryInfo |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsDefault](007f0409-9f60-03dd-758f-53fbda063f89.htm) | Determines if a ExportIFCCategoryInfo contains default information. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
