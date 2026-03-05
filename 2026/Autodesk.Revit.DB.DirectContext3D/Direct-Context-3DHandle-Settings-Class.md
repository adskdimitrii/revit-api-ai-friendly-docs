# Direct Context 3DHandle Settings Class

Source: https://www.revitapidocs.com/2026/cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm

---

| Direct Context 3DHandle Settings Class |
| --- |

Overriding settings applied to DirectContext3DHandles through the Visibility dialog. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.DirectContext3D DirectContext3DHandleSettings 
  
**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class DirectContext3DHandleSettings : IDisposable
```

```
Public Class DirectContext3DHandleSettings
	Implements IDisposable
```

```
public ref class DirectContext3DHandleSettings : IDisposable
```

```
type DirectContext3DHandleSettings = 
    class
        interface IDisposable
    end
```
The DirectContext3DHandleSettings type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DirectContext3DHandleSettings](3ae2b35d-7807-5218-497d-a39b982bc02c.htm) | Constructs an instance of settings with default values. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DirectContext3DHandleSettings(DirectContext3DHandleSettings)](da5944ec-af62-acbe-d39f-9bd7fe829ad8.htm) | Constructs a copy of source object. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [DirectContext3DHandleSettings(Boolean, Int32\)](a4fb006b-c127-be82-cd36-ad3004b892ac.htm) | Constructs an instance of settings with provided values. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](3aa923fb-a314-c5fd-c28d-d6aefe97f889.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Visibility](Direct-Context-3DHandle-Settings-Visibility-Property.md) | Visibility of the handle and the associated DirectContext3D graphics.  A value of true means that the graphics are visible. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Assign](1fc2a29d-9edb-a68c-c2f2-10fd2dd93374.htm) | Assigns values of the source settings to this object. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](d1ec6b05-f29c-be9c-2bd4-cd3c18491937.htm) | Releases all resources used by the DirectContext3DHandleSettings |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetColor](Direct-Context-3DHandle-Settings-Get-Color-Method.md) | Gets the color of the handle and the associated DirectContext3D graphics. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetTransparency](f8895d40-ca5e-5092-766b-4ad6150926f7.htm) | Gets the transparency value of the handle and the associated DirectContext3D graphics. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [IsEqual](54b1997b-1003-6f98-97f6-90fd2edb786e.htm) | Check if the contents of two instances of settings are equal. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetColor](Direct-Context-3DHandle-Settings-Set-Color-Method.md) | Sets the color of the handle and the associated DirectContext3D graphics. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetTransparency](26bfb243-1257-66ae-f25f-478902000415.htm) | Sets the transparency value of the handle and the associated DirectContext3D graphics. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetVisibility](Direct-Context-3DHandle-Settings-Set-Visibility-Method.md) | Visibility of the handle and the associated DirectContext3D graphics.  A value of true means that the graphics are visible. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks DirectContext3D graphics can be displayed with or without an associated DirectContext3D handle
 element. For DirectContext3D graphics that utilize the handle element, the visibility and appearance of
 the graphics can be adjusted through the Visibility/Graphics dialog. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)
