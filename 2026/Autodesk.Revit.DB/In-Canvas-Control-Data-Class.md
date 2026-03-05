# In Canvas Control Data Class

Source: https://www.revitapidocs.com/2026/5fdf010d-7dbb-332d-4704-8e067f2338dc.htm

---

| In Canvas Control Data Class |
| --- |

Represents a collection of data which is used by \[!:Autodesk::Revit::DB::TemporaryGraphicsManager] to create and update an in\-canvas control. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB InCanvasControlData 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class InCanvasControlData : IDisposable
```

```
Public Class InCanvasControlData
	Implements IDisposable
```

```
public ref class InCanvasControlData : IDisposable
```

```
type InCanvasControlData = 
    class
        interface IDisposable
    end
```
The InCanvasControlData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [InCanvasControlData(String)](3ab7de26-5e32-b3c7-0d35-5e739aad614c.htm) | Constructs an InCanvasControlData with specific values assigned. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [InCanvasControlData(String, XYZ)](f16cf225-d5a1-96e8-d036-bcda9f5dd8d1.htm) | Constructs an InCanvasControlData with specific values assigned. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ImagePath](35ae5240-5ed5-909b-9e89-3bd17eff90fd.htm) | The path to the image file to be used.  This must be an absolute path to a location on disk. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](c0d5263e-0680-9f7a-e084-79cbd6fbc6cb.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Position](aec870fe-2009-8281-ddb9-28c25d9909f2.htm) | The position of the in\-canvas control in model coordinates. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](a2fd1f89-85d4-a66f-52bc-241533915aff.htm) | Releases all resources used by the InCanvasControlData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks So far, only bitmap file is supported for [ImagePath](35ae5240-5ed5-909b-9e89-3bd17eff90fd.htm) . The rendered image is the same size
 in pixel dimensions as the original one. To get a better result, the caller should prepare the image with proper size, for exmaple: 32x32 or 64x64 in pixels,
 before use. To achive a "transparent" backgound color effect over the provided bitmap, the bitmap should use color RGB(0, 128, 128\) as its background and
 it will be cleared during rendering by Revit. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
