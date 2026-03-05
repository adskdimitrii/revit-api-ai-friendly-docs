# Nurbs Surface Data Class

Source: https://www.revitapidocs.com/2026/7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm

---

| Nurbs Surface Data Class |
| --- |

A class used to represent the definition of a NURBS surface. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB NurbsSurfaceData 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class NurbsSurfaceData : IDisposable
```

```
Public Class NurbsSurfaceData
	Implements IDisposable
```

```
public ref class NurbsSurfaceData : IDisposable
```

```
type NurbsSurfaceData = 
    class
        interface IDisposable
    end
```
The NurbsSurfaceData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [NurbsSurfaceData](6fdc9f8a-a443-a69f-2d9b-82cad9bf7544.htm) | Copy constructor. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DegreeU](fc2de49b-75ef-b407-cecf-3dd0199b775a.htm) | The degree of the spline in the u\-direction. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DegreeV](7bc890a0-c3d3-8e7f-5d9d-148a69de4813.htm) | The degree of the spline in the v\-direction. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsRational](da17256f-3c20-22c0-1619-5fe2d847752a.htm) | Tells if the spline is rational or not.  If it is true (rational), then the NURBS is a piecewise rational polynomial function.  If it is false (non\-rational), then the NURBS is a piecewise polynomial function. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](b9517067-344b-5d1b-8c5d-664b7e7115e1.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ReverseOrientation](57ca8156-bae7-58fc-89a4-88f08aa1f756.htm) | If true, the surface's orientation is opposite to the canonical parametric orientation, otherwise it is the same.  The canonical parametric orientation is a counter\-clockwise sense of rotation in the uv\-parameter plane.  Extrinsically, the oriented normal vector for the canonical parametric orientation points in the direction of  the cross product dS/du x dS/dv, which S(u, v) is the parameterized surface. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Create](94b4c433-5458-d1ab-d5c9-f526f288d1ff.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](27a918fc-a321-7712-4594-9dd7eb2d2140.htm) | Releases all resources used by the NurbsSurfaceData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetControlPoint](Nurbs-Surface-Data-Get-Control-Point-Method.md) | Get the list of control points. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetControlPoints](409fe43e-03a5-b9d6-5bf4-4f6427e3606e.htm) | Get the list of control points. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetKnotsU](e280fd98-bad6-3fb3-547f-a829ab23a9de.htm) | Get the list of knots in the u\-direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetKnotsV](1b0fea7f-4fd0-bee4-cc1b-773b13b2e36b.htm) | Get the list of knots in the v\-direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetKnotU](Nurbs-Surface-Data-Get-Knot-U-Method.md) | Get the knot in the u\-direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetKnotV](Nurbs-Surface-Data-Get-Knot-V-Method.md) | Get the knot in the v\-direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNumberOfControlPoints](Nurbs-Surface-Data-Get-Number-Of-Control-Points-Method.md) | Get the number of control points. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNumberOfKnotsU](Nurbs-Surface-Data-Get-Number-Of-Knots-U-Method.md) | Get the number of knots in the u\-direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNumberOfKnotsV](Nurbs-Surface-Data-Get-Number-Of-Knots-V-Method.md) | Get the number of knots in the v\-direction. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetNumberOfWeights](Nurbs-Surface-Data-Get-Number-Of-Weights-Method.md) | Get the number of weights. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetWeight](Nurbs-Surface-Data-Get-Weight-Method.md) | Get the weight. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetWeights](a1eec836-1db9-00ef-98eb-923c6a77a952.htm) | Get the list of weights. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsValid](6ca835bb-02f9-fe37-01ef-618310cef5ab.htm) | Check if the object contains a valid NurbsSurfaceData. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
