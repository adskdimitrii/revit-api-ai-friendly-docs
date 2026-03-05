# Slab Shape Editor Class

Source: https://www.revitapidocs.com/2026/06308ccc-46e7-6ff8-582c-6891af8b75e9.htm

---

| Slab Shape Editor Class |
| --- |

An object used for Slab Shape Editing. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB SlabShapeEditor 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class SlabShapeEditor : IDisposable
```

```
Public Class SlabShapeEditor
	Implements IDisposable
```

```
public ref class SlabShapeEditor : IDisposable
```

```
type SlabShapeEditor = 
    class
        interface IDisposable
    end
```
The SlabShapeEditor type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsEnabled](9aaaf1ca-5f52-c5be-9d5b-2230ad5131cc.htm) | Identifies if the slab shape editing functionality is enabled. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](ef4c3c30-e968-c860-8d38-ecfc2513f35f.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SlabShapeCreases](fb345daf-b097-a458-8c69-2d8cbfa1eff3.htm) | All of the creases that can be edited. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SlabShapeVertices](01fbf5d9-6fa7-6483-6a1c-5cf439f27dc7.htm) | All of the vertices that can be edited. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddPoint](5d875cfd-f401-6f88-cd07-3999543e8f18.htm) | Add a point to the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddPoints](52f630ac-2e57-4b33-7776-d499d469630d.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [AddSplitLine](2a254c45-4bff-9fbc-6ac0-680d79a3c88b.htm) | Add a split line to the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CreateCreasesFromFoldingLines](8adabb8c-e774-67c3-36a9-340cb8f0ab3f.htm) |  |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DeletePoint](4c1e94db-c98f-07e2-bd9b-8bb4feb1c66b.htm) | Delete a SlabShapeVertex from the element. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](093f82df-0da1-1021-1991-83094bc2f19d.htm) | Releases all resources used by the SlabShapeEditor |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Enable](792bbdb8-4629-7383-fbab-341df4b02341.htm) | Enables the slab shape editing functionality. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ModifySubElement(SlabShapeCrease, Double)](a2d107e1-fc23-5579-0d99-2ce20e41d207.htm) | Manipulates the crease on the corresponding slab, roof or floor. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ModifySubElement(SlabShapeVertex, Double)](844e2ab1-6c14-4b32-e6f0-ea23baa0ab5d.htm) | Manipulates the vertex on the corresponding slab, roof or floor. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [PickSupport](ff7dace3-8a34-3760-042d-21d1da8733f1.htm) | Picks an element to support the slab. This method will define split lines and create constant bearing lines for the slab. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [ResetSlabShape](b94ace8b-5eb5-a25d-6a18-5e23d8905911.htm) | Removes the modifications made during editing and resets the element geometry back to the unmodified state. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The SlabShapeEditor can be obtained from a slab object, such as a roof or floor. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
