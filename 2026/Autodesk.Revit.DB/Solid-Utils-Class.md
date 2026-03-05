# Solid Utils Class

Source: https://www.revitapidocs.com/2026/4c285bc6-c14e-9d55-5295-138764c01d12.htm

---

| Solid Utils Class |
| --- |

Contains utility functions for solid operations. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB SolidUtils 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static class SolidUtils
```

```
Public NotInheritable Class SolidUtils
```

```
public ref class SolidUtils abstract sealed
```

```
[<AbstractClassAttribute>]
[<SealedAttribute>]
type SolidUtils = class end
```
The SolidUtils type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Clone](2e985cf8-cdce-2045-c5d8-5a06fd49c002.htm) | Creates a new Solid which is a copy of the input Solid. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [ComputeIsGeometricallyClosed](Solid-Utils-Compute-Is-Geometrically-Closed-Method.md) | Computes whether the input Solid is geometrically closed to within Revit's tolerances. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [ComputeIsTopologicallyClosed](Solid-Utils-Compute-Is-Topologically-Closed-Method.md) | Compute whether the input Solid is topologically closed. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [CreateTransformed](22592761-f39c-4f53-d33b-6c21a4fa9d2d.htm) | Creates a new Solid which is the transformation of the input Solid. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [FindAllEdgeEndPointsAtVertex](4a7c822c-3be0-52b6-cdca-3cd6496759c5.htm) | Find all EdgeEndPoints at a vertex identified by the input EdgeEndPoint. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [IsValidForTessellation](a99a8a88-2e90-8d90-60bd-6ee37ab47515.htm) | Tests if the input solid or shell is valid for tessellation. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [SplitVolumes](0ba1e838-c300-ed47-bd2e-7fc3e2dd80d8.htm) | Splits a solid geometry into several separate solids. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [TessellateSolidOrShell](d856e5f0-2e26-f01a-2996-9fbc0ad1c03e.htm) | This function facets (i.e., triangulates) a solid or an open shell. Each boundary  component of the solid or shell is represented by a single triangulated structure. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
