# Ground Conductor Size Class

Source: https://www.revitapidocs.com/2026/922e6d1c-9bde-70c5-774b-a04a941003c1.htm

---

| Ground Conductor Size Class |
| --- |

**Note: This API is now obsolete.** 

Represents electrical ground conductor size definition information. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) 
Autodesk.Revit.DB.Electrical GroundConductorSize 
  
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("GroundConductorSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by GroundConductorSize properly during document upgrade.")]
public class GroundConductorSize : APIObject
```

```
<ObsoleteAttribute("GroundConductorSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by GroundConductorSize properly during document upgrade.")>
Public Class GroundConductorSize
	Inherits APIObject
```

```
[ObsoleteAttribute(L"GroundConductorSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by GroundConductorSize properly during document upgrade.")]
public ref class GroundConductorSize : public APIObject
```

```
[<ObsoleteAttribute("GroundConductorSize is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use ConductorSize instead. ConductorSizes will be created by GroundConductorSize properly during document upgrade.")>]
type GroundConductorSize = 
    class
        inherit APIObject
    end
```
The GroundConductorSize type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Ampacity](ae4fa6d0-70c4-3d32-94e2-9830317f5aad.htm) | Get ampacity which is used for specifying size, the unit is ampere. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ConductorSize](11897308-176b-ef3f-a791-8bbb3eb99cfe.htm) | Get conductor size corresponding to specific ampacity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read\-only or modifiable. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MaterialBelongTo](1a5ce82b-7509-7045-dca8-558f1ec98cb2.htm) | Get the material type which include this ground conductor size information. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Ground conductor size is defined based on corresponding wire material type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
