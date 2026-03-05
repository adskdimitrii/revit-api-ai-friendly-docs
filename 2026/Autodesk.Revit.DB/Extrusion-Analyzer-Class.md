# Extrusion Analyzer Class

Source: https://www.revitapidocs.com/2026/ba9e3283-6868-8834-e8bf-2ea9e7358930.htm

---

| Extrusion Analyzer Class |
| --- |

This geometry utility allows you to attempt to "fit" a given piece of solid geometry into
 the shape of an extrusion. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB ExtrusionAnalyzer 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class ExtrusionAnalyzer : IDisposable
```

```
Public Class ExtrusionAnalyzer
	Implements IDisposable
```

```
public ref class ExtrusionAnalyzer : IDisposable
```

```
type ExtrusionAnalyzer = 
    class
        interface IDisposable
    end
```
The ExtrusionAnalyzer type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndParameter](bebcd422-84f8-2086-d130-ef04abab4d64.htm) | The end parameter (distance along the extrusion direction from the input plane) calculated by the extrusion analysis. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ExtrusionDirection](556d164b-2d06-1bcf-d95a-6fa068db5745.htm) | The direction of extrusion specified for the extrusion analysis. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](d551619e-f297-4d50-5d61-51d217663502.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [StartParameter](7d4e2c44-7021-7d94-de0f-e964447b17bb.htm) | The start parameter (distance along the extrusion direction from the input plane) calculated by the extrusion analysis. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CalculateFaceAlignment](7e51ca19-05ec-82e1-905d-df564b15a7d8.htm) | Calculates the alignment status of each face of the solid. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method")![Static member](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/static.gif "Static member") | [Create](Extrusion-Analyzer-Create-Method.md) | Creates an ExtrusionAnalyzer and computes and stores the Solid's shadow. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](5a8adeed-72ce-9eae-eca0-1d7225fcf2c5.htm) | Releases all resources used by the ExtrusionAnalyzer |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetExtrusionBase](3e24586d-4a80-5331-8e79-74d1b6249ca6.htm) | Obtains the face that represents the base contour of the extrusion analysis. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks An instance of this class is a single\-time use class which should be provided a
 solid geometry, a plane, and a direction. The utility will calculate a base boundary
 parallel to the input plane which is the outer boundary of the shadow cast by the
 Solid onto the input plane and along the extrusion direction. 

After the extrusion has been calculated, the class permits a second step
 analysis to identify all faces from the original geometry which do not align with the
 faces of the calculated extrusion. 

This utility works best for a Solid that is at least somewhat "extrusion\-like",
 for example, the geometry of a wall which may or may not be affected by end joins,
 floor joins, roof joins, openings cut by windows and doors, or other
 modifications. 

The ExtrusionAnalyzer expects only one single extrusion\-like solid geometry.
 The ExtrusionAnalyzer does not support a Solid containing multiple distinguishable "lumps" of geometry
 and may give unexpected results in such cases.
 In such cases, consider splitting the Solid into its individual connected commponent using \[!:Autodesk::Revit::DB::SolidUtils::SplitVolumes] before performing an extrusion analysis. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
