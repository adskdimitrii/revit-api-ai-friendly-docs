# Correction Factor Class

Source: https://www.revitapidocs.com/2026/203305c0-061a-5607-9f94-5d0cb9a2ca06.htm

---

| Correction Factor Class |
| --- |

**Note: This API is now obsolete.** 

Represents electrical correction factor information. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) 
Autodesk.Revit.DB.Electrical CorrectionFactor 
  
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("CorrectionFactor is deprecated in Revit 2026 and will be removed in a future version of Revit. There is no replacement because Revit no longer supports this.")]
public class CorrectionFactor : APIObject
```

```
<ObsoleteAttribute("CorrectionFactor is deprecated in Revit 2026 and will be removed in a future version of Revit. There is no replacement because Revit no longer supports this.")>
Public Class CorrectionFactor
	Inherits APIObject
```

```
[ObsoleteAttribute(L"CorrectionFactor is deprecated in Revit 2026 and will be removed in a future version of Revit. There is no replacement because Revit no longer supports this.")]
public ref class CorrectionFactor : public APIObject
```

```
[<ObsoleteAttribute("CorrectionFactor is deprecated in Revit 2026 and will be removed in a future version of Revit. There is no replacement because Revit no longer supports this.")>]
type CorrectionFactor = 
    class
        inherit APIObject
    end
```
The CorrectionFactor type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Factor](cd4158ad-f037-5170-cde2-bbc1ba2427bf.htm) | Get factor value of wire correction factor. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsReadOnly](d516bcd2-a3fd-a578-58f6-f1add979bd07.htm) | Identifies if the object is read\-only or modifiable. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7c03212a-b587-1c89-3912-efea0d2619c5.htm) | Causes the object to release immediately any resources it may be utilizing. (Inherited from [APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTemperature](5d5653ab-6b66-fb08-ae26-5c7bba5102a8.htm) | Get temperature which is used for specifying correction factor. The value returned is quantified in the document's selected unit of electrical temperature. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Correction factor is defined based on corresponding wire material type and temperature rating type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
