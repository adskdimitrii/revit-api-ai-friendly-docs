# IFCProperty Mapping Info Class

Source: https://www.revitapidocs.com/2026/dc749207-a8f4-9e72-b7ea-e6aa157bb712.htm

---

| IFCProperty Mapping Info Class |
| --- |

Represents the IFC property mapping information stored in the template. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB IFCPropertyMappingInfo 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class IFCPropertyMappingInfo : IDisposable
```

```
Public Class IFCPropertyMappingInfo
	Implements IDisposable
```

```
public ref class IFCPropertyMappingInfo : IDisposable
```

```
type IFCPropertyMappingInfo = 
    class
        interface IDisposable
    end
```
The IFCPropertyMappingInfo type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IFCPropertyMappingInfo](IFCProperty-Mapping-Info-Constructor-2.md) | Constructs a new IFCPropertyMappingInfo with default values. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IFCPropertyMappingInfo(Boolean, String, ElementId, String)](IFCProperty-Mapping-Info-Boolean-String-Element-Id-String-Constructor.md) | Constructs a new IFCPropertyMappingInfo with input values.  The flag that indicates whether the property is included in export.  The property name.  The Revit property id.  The Revit property id. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ExportFlag](IFCProperty-Mapping-Info-Export-Flag-Property.md) | Whether or not the property is included in export. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IFCPropertyName](IFCProperty-Mapping-Info-IFCProperty-Name-Property.md) | The IFC property name. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](IFCProperty-Mapping-Info-Is-Valid-Object-Property.md) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RevitPropertyId](IFCProperty-Mapping-Info-Revit-Property-Id-Property.md) | The Revit property id. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [RevitPropertyName](IFCProperty-Mapping-Info-Revit-Property-Name-Property.md) | The Revit property name. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](IFCProperty-Mapping-Info-Dispose-Method.md) | Releases all resources used by the IFCPropertyMappingInfo |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsValidMappingInfo](IFCProperty-Mapping-Info-Is-Valid-Mapping-Info-Method.md) | Defines whether the mapping info contains meaningful data. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
