# Wire Size Class

Source: https://www.revitapidocs.com/2026/e4a5cfed-7952-4622-5fca-b556703e36b6.htm

---

| Wire Size Class |
| --- |

**Note: This API is now obsolete.** 

Represents specific electrical wire size information. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) 
Autodesk.Revit.DB.Electrical WireSize 
  
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("WireSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by WireSizes properly during document upgrade.")]
public class WireSize : APIObject
```

```
<ObsoleteAttribute("WireSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by WireSizes properly during document upgrade.")>
Public Class WireSize
	Inherits APIObject
```

```
[ObsoleteAttribute(L"WireSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by WireSizes properly during document upgrade.")]
public ref class WireSize : public APIObject
```

```
[<ObsoleteAttribute("WireSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by WireSizes properly during document upgrade.")>]
type WireSize = 
    class
        inherit APIObject
    end
```
The WireSize type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Ampacity](88ae5dbc-6d26-3db2-f7c2-e0a3e49920db.htm) | Get ampacity which be used for specifying size, the unit is ampere. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Diameter](e4a9047e-c2ed-db31-9e62-b0efc14180c3.htm) | Get diameter of wire. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [InUse](c342629c-66db-7051-d8de-314c6a7779dc.htm) | Get or set whether the size can be used in sizing. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read\-only or modifiable. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Size](9cbe7525-130e-142e-e0ad-31a66385cc08.htm) | Get size symbol of wire. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Wire size is defined based on corresponding wire material type and temperature rating type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
