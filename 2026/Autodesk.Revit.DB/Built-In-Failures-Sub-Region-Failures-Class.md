# Built In Failures Sub Region Failures Class

Source: https://www.revitapidocs.com/2026/da08085c-3c91-d0cc-0b94-117b82fa132c.htm

---

| Built In Failures Sub Region Failures Class |
| --- |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB BuiltInFailures SubRegionFailures 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static class SubRegionFailures
```

```
Public NotInheritable Class SubRegionFailures
```

```
public ref class SubRegionFailures abstract sealed
```

```
[<AbstractClassAttribute>]
[<SealedAttribute>]
type SubRegionFailures = class end
```
The BuiltInFailures SubRegionFailures type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [CreateSubRegionFailed](5e5b3a13-20b0-1b4d-1724-05c2a60e06fd.htm) | Create sub\-division failed. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [NoHostForToposolidSubregion](22a279c7-90e2-b02e-ee45-65120079a363.htm) | This sub\-division now does not appear to overlap any Toposolid with an appropriate Phase and Design Option. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [SubDivisionOffsetInvalid](Built-In-Failures-Sub-Region-Failures-Sub-Division-Offset-Invalid-Property.md) | Sub\-division's offset must be less than the thickness of its type. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [SubDivisionPhaseMismatch](e8d845a6-4c54-aba8-1ff7-7d51189c2874.htm) | Sub\-division must have the same Phase Created parameter and Phase Demolished parameter as the host Toposolid. Sub\-division phase will be set to match the Toposolid. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
